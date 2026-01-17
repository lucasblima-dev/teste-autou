import { ZapIcon } from 'lucide-react';

export function App() {
  return (
    <div className="bg-gray-900 min-h-screen text-gray-200 flex flex-col items-center justify-center p-4 font-sans">
      <div className="w-full max-w-2xl mx-auto">
        <header className="text-center mb-8">
          <div className="flex items-center justify-center gap-3 mb-2">
            <ZapIcon className="text-blue-500" size={32} />
            <h1 className="text-4xl font-bold text-white">AutoU Classifier</h1>
          </div>
          <p className="text-lg text-gray-400">
            Cole um email ou carregue um arquivo para classificá-lo com IA.
          </p>
        </header>

        <main className="bg-gray-800 border border-gray-700 rounded-xl shadow-lg p-6 sm:p-8">
        </main>

        {/*
        <footer className="text-center mt-8">
          <a
            href="https://github.com/user/repositório"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-2 text-gray-500 hover:text-gray-400 transition-colors"
          >
            <GithubIcon size={16} />
            <span>Ver código no GitHub</span>
          </a>
        </footer>
        */}
      </div>
    </div>
  );
}