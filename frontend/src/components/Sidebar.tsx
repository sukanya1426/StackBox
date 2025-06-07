"use client";
import Link from 'next/link';

export default function Sidebar() {
  return (
    <aside className="w-64 bg-white dark:bg-gray-800 shadow-lg h-screen">
      <div className="p-6">
        <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">
          File Manager
        </h2>
        <nav>
          <ul className="space-y-2">
            <li>
              <Link href="/dashboard" className="block py-2 px-4 text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-700 rounded">
                Dashboard
              </Link>
            </li>
            <li>
              <Link href="#" className="block py-2 px-4 text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-700 rounded">
                Profile
              </Link>
            </li>
          </ul>
        </nav>
      </div>
    </aside>
  );
}