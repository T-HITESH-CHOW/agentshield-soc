import * as React from "react"
import { cn } from "@/lib/utils"

export interface BadgeProps extends React.HTMLAttributes<HTMLDivElement> {
  variant?: "default" | "secondary" | "destructive" | "outline" | "cyan" | "amber" | "green"
}

function Badge({ className, variant = "default", ...props }: BadgeProps) {
  const variants: Record<string, string> = {
    default: "border-transparent bg-slate-100 text-slate-900 hover:bg-slate-100/80",
    secondary: "border-transparent bg-slate-800 text-slate-100 hover:bg-slate-800/80",
    destructive: "border-transparent bg-red-900 text-slate-100 hover:bg-red-900/80",
    outline: "text-slate-100 border-slate-800",
    cyan: "border-transparent bg-cyan-900/50 text-cyan-400 border border-cyan-800",
    amber: "border-transparent bg-amber-900/50 text-amber-400 border border-amber-800",
    green: "border-transparent bg-green-900/50 text-green-400 border border-green-800",
  }
  
  return (
    <div className={cn("inline-flex items-center rounded-md border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-slate-950 focus:ring-offset-2", variants[variant], className)} {...props} />
  )
}

export { Badge }
