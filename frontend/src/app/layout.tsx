import { Header, Footer } from '@/components/Header';
import Sidebar from '@/components/Sidebar';
import '../styles/globals.css'; // Import global styles

export const metadata = {
  title: 'File Manager Dashboard',
  description: 'A sleek file management dashboard built with Next.js and FastAPI',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className="antialiased flex flex-col min-h-screen">
        <div className="flex flex-1">
          <Sidebar />
          <div className="flex-1 flex flex-col">
            <Header />
            <main className="flex-grow p-6 bg-gray-100 dark:bg-gray-900">
              {children}
            </main>
            <Footer />
          </div>
        </div>
      </body>
    </html>
  );
}