import axios from 'axios';
import { ZapIcon } from 'lucide-react';
import { useState } from 'react';

import type { ApiResult } from './types/Api.types';
import { EmailForm } from './components/EmailForm';
import { ShowResult } from './components/ShowResult';

export function App() {
  const [emailText, setEmailText] = useState('');
  const [result, setResult] = useState<ApiResult | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleClear = () => {
    setEmailText('');
    setResult(null);
    setError(null);
    setIsLoading(false);
  };

  const handleSubmit = async () => {
    if (!emailText.trim()) {
      setError("Por favor, insira o texto de um email para analisar.");
      return;
    }
    setIsLoading(true);
    setError(null);
    setResult(null);
    try {
      const apiUrl = `${import.meta.env.VITE_API_BASE_URL}/api/classify`;
      const response = await axios.post<ApiResult>(apiUrl, {
        text: emailText,
      });
      setResult(response.data);
      // eslint-disable-next-line @typescript-eslint/no-unused-vars
    } catch (err) {
      //console.error("Erro na chamada da API:", err);
      setError("Ocorreu um erro ao analisar o email. Tente novamente e se o problema persistir, contate os responsáveis.");
    } finally {
      setIsLoading(false);
    }
  };

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
          <EmailForm
            emailText={emailText}
            setEmailText={setEmailText}
            onSubmit={handleSubmit}
            isLoading={isLoading}
            onClear={handleClear}
          />

          {error && (
            <div className="mt-6 p-4 bg-red-900/50 border border-red-700 text-red-300 rounded-lg">
              {error}
            </div>
          )}

          {result && !isLoading && (
            <div className="mt-6">
              <ShowResult result={result} />
            </div>
          )}
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