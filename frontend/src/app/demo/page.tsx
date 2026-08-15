'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';

const SAMPLE_CONTENT = {
  blog: `The Future of AI in Content Creation

Artificial Intelligence is revolutionizing the way we create content. From blog posts to social media updates, AI tools are helping writers produce high-quality material in a fraction of the time.

Key Benefits:
• Speed: Generate drafts in seconds
• Consistency: Maintain brand voice across all content  
• Creativity: Overcome writer's block with fresh ideas
• SEO: Optimize content for search engines automatically

As we move forward, the collaboration between human creativity and AI efficiency will define the next era of digital content.`,

  social: `🚀 Just discovered how AI can 10x my content output!

✅ Blog posts in 2 minutes
✅ Social captions that actually engage  
✅ Email newsletters people READ

The future isn't replacing writers—it's empowering them.

What's your take on AI tools? 👇

#AI #ContentCreation #Productivity`,

  email: `Subject: Your Weekly Content Strategy Update

Hi [Name],

I hope this email finds you well. I wanted to share some exciting updates about our content strategy this month.

Our AI-powered content system has helped us:
• Publish 3x more blog posts
• Increase engagement by 45%
• Save 20+ hours per week

I've attached our latest content calendar for your review. Let me know if you'd like to schedule a call to discuss.

Best regards,
[Your Name]`
};

export default function DemoPage() {
  const router = useRouter();
  const [activeType, setActiveType] = useState<'blog' | 'social' | 'email'>('blog');
  const [isGenerating, setIsGenerating] = useState(false);
  const [showOutput, setShowOutput] = useState(false);

  const handleGenerate = () => {
    setIsGenerating(true);
    setShowOutput(false);
    
    // Simulate AI generation with typing effect
    setTimeout(() => {
      setIsGenerating(false);
      setShowOutput(true);
    }, 1500);
  };

  const contentTypes = [
    { id: 'blog', label: 'Blog Post', icon: '📝' },
    { id: 'social', label: 'Social Media', icon: '📱' },
    { id: 'email', label: 'Email', icon: '📧' }
  ] as const;

  return (
    <div className="min-h-screen bg-black text-white">
      {/* Navbar */}
      <nav className="flex justify-between items-center p-6 border-b border-gray-800">
        <a href="/" className="text-2xl font-bold tracking-tight">AI Content Generator</a>
        <div className="space-x-4">
          <a href="/auth/login" className="text-gray-300 hover:text-white transition">Sign In</a>
          <a href="/auth/register" className="bg-white text-black px-4 py-2 rounded-lg font-medium hover:bg-gray-200 transition">
            Get Started Free
          </a>
        </div>
      </nav>

      <div className="max-w-6xl mx-auto px-4 py-12">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-4xl md:text-5xl font-bold mb-4">See It In Action</h1>
          <p className="text-gray-400 text-lg max-w-2xl mx-auto">
            Watch how AI generates professional content in seconds. No signup required for this demo.
          </p>
        </div>

        {/* Demo Interface */}
        <div className="grid md:grid-cols-2 gap-8">
          {/* Left: Input Panel */}
          <div className="border border-gray-800 rounded-2xl p-6 bg-gray-900/50">
            <h2 className="text-xl font-semibold mb-6">1. Choose Content Type</h2>
            
            <div className="grid grid-cols-3 gap-3 mb-6">
              {contentTypes.map((type) => (
                <button
                  key={type.id}
                  onClick={() => {
                    setActiveType(type.id);
                    setShowOutput(false);
                  }}
                  className={`p-3 rounded-xl border transition text-center ${
                    activeType === type.id
                      ? 'border-white bg-white/10'
                      : 'border-gray-700 hover:border-gray-500'
                  }`}
                >
                  <div className="text-2xl mb-1">{type.icon}</div>
                  <div className="text-sm font-medium">{type.label}</div>
                </button>
              ))}
            </div>

            <div className="mb-6">
              <label className="block text-sm font-medium text-gray-300 mb-2">Topic</label>
              <input
                type="text"
                value="The Future of AI in Content Creation"
                readOnly
                className="w-full bg-black border border-gray-700 rounded-lg px-4 py-3 text-gray-300"
              />
            </div>

            <div className="mb-6">
              <label className="block text-sm font-medium text-gray-300 mb-2">Tone</label>
              <select 
                disabled
                className="w-full bg-black border border-gray-700 rounded-lg px-4 py-3 text-gray-300"
              >
                <option>Professional</option>
              </select>
            </div>

            <button
              onClick={handleGenerate}
              disabled={isGenerating}
              className="w-full bg-white text-black font-bold py-3 rounded-lg hover:bg-gray-200 transition disabled:opacity-50 flex items-center justify-center gap-2"
            >
              {isGenerating ? (
                <>
                  <div className="w-5 h-5 border-2 border-black border-t-transparent rounded-full animate-spin" />
                  AI is writing...
                </>
              ) : (
                <>
                  ✨ Generate Content
                </>
              )}
            </button>
          </div>

          {/* Right: Output Panel */}
          <div className="border border-gray-800 rounded-2xl p-6 bg-gray-900/50 min-h-[400px]">
            <div className="flex justify-between items-center mb-6">
              <h2 className="text-xl font-semibold">2. Generated Output</h2>
              {showOutput && (
                <div className="flex gap-2">
                  <button 
                    onClick={() => navigator.clipboard.writeText(SAMPLE_CONTENT[activeType])}
                    className="text-xs bg-gray-800 px-3 py-1 rounded hover:bg-gray-700 transition"
                  >
                    Copy
                  </button>
                </div>
              )}
            </div>

            {!showOutput && !isGenerating && (
              <div className="flex flex-col items-center justify-center h-64 text-gray-500">
                <div className="text-4xl mb-4">🤖</div>
                <p>Click "Generate Content" to see AI magic</p>
              </div>
            )}

            {isGenerating && (
              <div className="flex flex-col items-center justify-center h-64">
                <div className="w-12 h-12 border-4 border-white border-t-transparent rounded-full animate-spin mb-4" />
                <p className="text-gray-400 animate-pulse">Crafting your content...</p>
                <div className="mt-4 flex gap-1">
                  {[...Array(3)].map((_, i) => (
                    <div
                      key={i}
                      className="w-2 h-2 bg-white rounded-full animate-bounce"
                      style={{ animationDelay: `${i * 0.2}s` }}
                    />
                  ))}
                </div>
              </div>
            )}

            {showOutput && (
              <div className="animate-fade-in">
                <div className="bg-black border border-gray-800 rounded-xl p-4 mb-4">
                  <pre className="whitespace-pre-wrap text-gray-300 text-sm leading-relaxed font-sans">
                    {SAMPLE_CONTENT[activeType]}
                  </pre>
                </div>
                <div className="flex justify-between text-sm text-gray-500">
                  <span>Word count: {SAMPLE_CONTENT[activeType].split(/\s+/).length}</span>
                  <span className="text-green-400">✓ Generated in 1.2s</span>
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Features Grid */}
        <div className="mt-16 grid md:grid-cols-3 gap-6">
          <div className="border border-gray-800 rounded-xl p-6 text-center">
            <div className="text-3xl mb-3">⚡</div>
            <h3 className="font-bold mb-2">Lightning Fast</h3>
            <p className="text-gray-400 text-sm">Generate blog posts, emails, and social content in under 10 seconds.</p>
          </div>
          <div className="border border-gray-800 rounded-xl p-6 text-center">
            <div className="text-3xl mb-3">🎯</div>
            <h3 className="font-bold mb-2">Multiple Tones</h3>
            <p className="text-gray-400 text-sm">Professional, casual, persuasive, or funny—match your brand voice.</p>
          </div>
          <div className="border border-gray-800 rounded-xl p-6 text-center">
            <div className="text-3xl mb-3">💾</div>
            <h3 className="font-bold mb-2">Save History</h3>
            <p className="text-gray-400 text-sm">All your generated content saved securely for future access.</p>
          </div>
        </div>

        {/* CTA */}
        <div className="mt-16 text-center border border-gray-800 rounded-2xl p-8">
          <h2 className="text-2xl font-bold mb-4">Ready to create your own?</h2>
          <p className="text-gray-400 mb-6">Get 5 free credits when you sign up today.</p>
          <div className="flex gap-4 justify-center">
            <a href="/auth/register" className="bg-white text-black px-8 py-3 rounded-lg font-bold hover:bg-gray-200 transition">
              Start Writing Free
            </a>
            <a href="/" className="border border-gray-600 px-8 py-3 rounded-lg font-bold hover:border-white transition">
              Back to Home
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}