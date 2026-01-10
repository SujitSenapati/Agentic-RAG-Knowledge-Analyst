import axios from 'axios'

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

interface AgentResponse {
  answer: string
  trace: any
}

export async function askAgent(question: string): Promise<AgentResponse> {
  try {
    const response = await axios.post(`${API_BASE_URL}/api/ask`, {
      question,
    })
    
    return response.data
  } catch (error) {
    if (axios.isAxiosError(error)) {
      throw new Error(error.response?.data?.detail || 'Failed to get response from agent')
    }
    throw error
  }
}
