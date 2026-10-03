export default function Home() {
  return (
    <main className="flex min-h-screen items-center justify-center bg-slate-950 px-6 text-slate-100">
      <section className="w-full max-w-xl rounded-2xl border border-slate-800 bg-slate-900 p-10 shadow-2xl">
        <p className="mb-3 text-sm font-semibold uppercase tracking-[0.3em] text-cyan-400">
          VYNX
        </p>
        <h1 className="text-4xl font-bold tracking-tight">Local Media Utility</h1>
        <p className="mt-8 text-sm text-slate-400">Backend status:</p>
        <p className="mt-1 text-lg text-amber-300">Not connected yet</p>
      </section>
    </main>
  );
}

