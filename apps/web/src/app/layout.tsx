import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'
import { AppShell } from '@/components/layout/AppShell'
import { cn } from '@/lib/utils'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'AgentShield SOC',
  description: 'Evidence-first, evaluation-driven AI SOC platform',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className="dark">
      <body className={cn("bg-slate-950 text-slate-300 antialiased h-screen overflow-hidden", inter.className)}>
        <AppShell>{children}</AppShell>
      </body>
    </html>
  )
}
