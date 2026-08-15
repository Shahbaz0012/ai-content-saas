export default function Home() {
  return (
    <main className="min-h-screen bg-black text-white">
      {/* Navbar */}
      <nav className="flex justify-between items-center p-6 border-b border-gray-800">
        <h1 className="text-2xl font-bold tracking-tight">AI Content Generator</h1>
        <div className="space-x-4">
          <a href="/auth/login" className="text-gray-300 hover:text-white transition">Sign In</a>
          <a href="/auth/register" className="bg-white text-black px-4 py-2 rounded-lg font-medium hover:bg-gray-200 transition">
            Get Started
          </a>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="flex flex-col items-center justify-center text-center px-4 py-24">
        <h2 className="text-5xl md:text-7xl font-bold mb-6 leading-tight">
          Create Content That <span className="text-gray-400">Converts</span>
        </h2>
        <p className="text-xl text-gray-400 max-w-2xl mb-10 leading-relaxed">
          Generate blogs, social posts, emails, and more in seconds with AI. 
          Professional content without the writer's block.
        </p>
        <div className="flex gap-4">
          <a 
            href="/auth/register" 
            className="bg-white text-black px-8 py-3 rounded-lg font-bold text-lg hover:bg-gray-200 transition min-w-[180px] text-center"
          >
            Start Writing Free
          </a>
          <a 
            href="/demo" 
            className="border border-gray-600 px-8 py-3 rounded-lg font-bold text-lg hover:border-white transition min-w-[180px] text-center"
          >
            See Demo
          </a>
        </div>
      </section>
    </main>
  );
}