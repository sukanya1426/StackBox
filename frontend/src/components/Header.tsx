"use client";

import { useTheme } from 'next-themes';
import { useEffect, useState } from 'react';

export function Header() {
  const { theme, setTheme } = useTheme();
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  if (!mounted) return null;

  return (
    <header className="bg-white dark:bg-gray-800 shadow-md">
      <div className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
        <h1 className="text-xl font-bold text-gray-900 dark:text-white">
          File Manager
        </h1>
        <button
          onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
          className="p-2 rounded-full bg-gray-200 dark:bg-gray-600 text-gray-800 dark:text-gray-200 hover:bg-gray-300 dark:hover:bg-gray-500 transition-colors"
        >
          {theme === 'dark' ? '🌞 Light' : '🌙 Dark'}
        </button>
      </div>
    </header>
  );
}

export function Footer() {
  return (
    <footer className="bg-white dark:bg-gray-800 shadow-inner">
      <div className="max-w-7xl mx-auto px-4 py-4 text-center">
        <p className="text-gray-600 dark:text-gray-400">
          © {new Date().getFullYear()} File Manager. All rights reserved.
        </p>
      </div>
    </footer>
  );
}