'use client';

import React, { useState, useEffect } from 'react';

interface FileEntry {
  id: number;
  filename: string;
  content_type: string;
  size: number;
  uploaded_at: string;
}

export default function Dashboard() {
  const [file, setFile] = useState<File | null>(null);
  const [files, setFiles] = useState<FileEntry[]>([]);
  const [message, setMessage] = useState<{ text: string; type: 'success' | 'error' } | null>(null);

  useEffect(() => {
    fetchFiles();
  }, []);

  const fetchFiles = async () => {
    try {
      const response = await fetch('http://localhost:8000/list-files', { mode: 'cors' });
      if (!response.ok) throw new Error('Failed to fetch files');
      const data = await response.json();
      setFiles(data);
    } catch (error) {
      const errorMsg = error instanceof Error ? error.message : String(error);
      setMessage({ text: 'Error fetching files: ' + errorMsg, type: 'error' });
    }
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      setFile(e.target.files[0]);
    }
  };

  const handleUpload = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!file) {
      setMessage({ text: 'Please select a file to upload', type: 'error' });
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:8000/upload', {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || 'Upload failed');
      setMessage({ text: 'File uploaded successfully', type: 'success' });
      setFile(null);
      fetchFiles();
    } catch (error) {
      const errorMsg = error instanceof Error ? error.message : String(error);
      setMessage({ text: 'Upload failed: ' + errorMsg, type: 'error' });
    }
  };

  const handleDownload = async (filename: string) => {
    try {
      window.location.href = `http://localhost:8000/download/${filename}`;
    } catch (error) {
      const errorMsg = error instanceof Error ? error.message : String(error);
      setMessage({ text: 'Download failed: ' + errorMsg, type: 'error' });
    }
  };

  const handleDelete = async (filename: string) => {
    if (!confirm(`Are you sure you want to delete ${filename}?`)) return;

    try {
      const response = await fetch(`http://localhost:8000/delete/${filename}`, {
        method: 'DELETE',
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || 'Deletion failed');
      setMessage({ text: data.message, type: 'success' });
      fetchFiles();
    } catch (error) {
      const errorMsg = error instanceof Error ? error.message : String(error);
      setMessage({ text: 'Deletion failed: ' + errorMsg, type: 'error' });
    }
  };

  return (
    <div className="container mx-auto">
      <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg mb-6">
        <h2 className="text-2xl font-semibold text-gray-900 dark:text-white mb-4">
          File Management Dashboard
        </h2>
        <form onSubmit={handleUpload} className="mb-6">
          <div className="flex items-center space-x-4">
            <input
              type="file"
              onChange={handleFileChange}
              className="flex-grow p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-gray-200"
            />
            <button
              type="submit"
              className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors"
            >
              Upload
            </button>
          </div>
        </form>
        {message && (
          <div
            className={`mb-6 p-4 rounded-md text-white ${
              message.type === 'success' ? 'bg-green-500' : 'bg-red-500'
            }`}
          >
            {message.text}
          </div>
        )}
      </div>
      <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg">
        <h3 className="text-xl font-medium text-gray-900 dark:text-white mb-4">
          Uploaded Files
        </h3>
        {files.length === 0 ? (
          <p className="text-gray-600 dark:text-gray-400 text-center">
            No files uploaded yet.
          </p>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {files.map((file) => (
              <div
                key={file.id}
                className="p-4 bg-gray-50 dark:bg-gray-700 rounded-md shadow flex justify-between items-center"
              >
                <div>
                  <p className="text-gray-900 dark:text-gray-200 font-medium">
                    {file.filename}
                  </p>
                  <p className="text-sm text-gray-600 dark:text-gray-400">
                    {new Date(file.uploaded_at).toLocaleString()} •{' '}
                    {(file.size / 1024).toFixed(2)} KB
                  </p>
                </div>
                <div className="flex space-x-2">
                  <button
                    onClick={() => handleDownload(file.filename)}
                    className="px-3 py-1 bg-green-600 text-white rounded-md hover:bg-green-700 transition-colors"
                  >
                    Download
                  </button>
                  <button
                    onClick={() => handleDelete(file.filename)}
                    className="px-3 py-1 bg-red-600 text-white rounded-md hover:bg-red-700 transition-colors"
                  >
                    Delete
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}