'use client'

import { useState } from 'react'
import ReactMarkdown from 'react-markdown'
import { askAgent } from '@/lib/api'

interface AgentTrace {
  plan?: string[]
  tools_used?: string[]
  [key: string]: any
}

export default function AgentInterface() {
  const [question, setQuestion] = useState('')
  const [answer, setAnswer] = useState('')
  const [trace, setTrace] = useState<AgentTrace | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    
    if (!question.trim()) {
      return
    }

    setLoading(true)
    setError('')
    setAnswer('')
    setTrace(null)

    try {
      const response = await askAgent(question)
      setAnswer(response.answer)
      setTrace(response.trace)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="max-w-6xl mx-auto">
      {/* Header */}
      <div className="mb-8 text-center">
        <h1 className="text-4xl font-bold mb-2 bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
          Agentic RAG – Enterprise Knowledge Analyst
        </h1>
        <p className="text-gray-600 dark:text-gray-400">
          Ask about Kubernetes, incidents, compliance, or APIs
        </p>
      </div>

      {/* Question Input Form */}
      <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 mb-6">
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label htmlFor="question" className="block text-sm font-medium mb-2 text-gray-700 dark:text-gray-300">
              Question
            </label>
            <textarea
              id="question"
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              placeholder="Ask about Kubernetes, incidents, compliance, or APIs..."
              className="w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg 
                       focus:ring-2 focus:ring-blue-500 focus:border-transparent
                       bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100
                       placeholder-gray-400 dark:placeholder-gray-500
                       resize-none transition-all"
              rows={3}
              disabled={loading}
            />
          </div>
          
          <button
            type="submit"
            disabled={loading || !question.trim()}
            className="w-full bg-gradient-to-r from-blue-600 to-purple-600 
                     text-white font-semibold py-3 px-6 rounded-lg
                     hover:from-blue-700 hover:to-purple-700
                     disabled:from-gray-400 disabled:to-gray-500 disabled:cursor-not-allowed
                     transition-all duration-200 shadow-md hover:shadow-lg
                     transform hover:scale-[1.02] active:scale-[0.98]"
          >
            {loading ? (
              <span className="flex items-center justify-center">
                <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Processing...
              </span>
            ) : (
              'Ask Agent'
            )}
          </button>
        </form>
      </div>

      {/* Error Message */}
      {error && (
        <div className="bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 
                      rounded-lg p-4 mb-6">
          <p className="text-red-800 dark:text-red-200 font-medium">Error: {error}</p>
        </div>
      )}

      {/* Answer Section */}
      {answer && (
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 mb-6">
          <h2 className="text-xl font-semibold mb-4 text-gray-800 dark:text-gray-200 
                       border-b border-gray-200 dark:border-gray-700 pb-2">
            Answer
          </h2>
          <div className="prose dark:prose-invert max-w-none 
                        prose-headings:text-gray-800 dark:prose-headings:text-gray-200
                        prose-p:text-gray-700 dark:prose-p:text-gray-300
                        prose-a:text-blue-600 dark:prose-a:text-blue-400
                        prose-code:text-purple-600 dark:prose-code:text-purple-400
                        prose-pre:bg-gray-100 dark:prose-pre:bg-gray-900">
            <ReactMarkdown>{answer}</ReactMarkdown>
          </div>
        </div>
      )}

      {/* Agent Trace Section */}
      {trace && (
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6">
          <h2 className="text-xl font-semibold mb-4 text-gray-800 dark:text-gray-200 
                       border-b border-gray-200 dark:border-gray-700 pb-2">
            Agent Trace
          </h2>
          <div className="bg-gray-50 dark:bg-gray-900 rounded-lg p-4 overflow-x-auto">
            <pre className="text-sm text-gray-800 dark:text-gray-200 whitespace-pre-wrap">
              {JSON.stringify(trace, null, 2)}
            </pre>
          </div>
        </div>
      )}
    </div>
  )
}
