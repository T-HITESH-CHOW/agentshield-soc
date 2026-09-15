'use client'
import Link from "next/link"
import { usePathname } from "next/navigation"
import { Shield, LayoutDashboard, Bell, FolderOpen, Search, FlaskConical, BarChart3, Settings } from "lucide-react"
import { cn } from "@/lib/utils"

const navigation = [
  { name: 'Dashboard', href: '/dashboard', icon: LayoutDashboard },
  { name: 'Alerts', href: '/alerts', icon: Bell },
  { name: 'Cases', href: '/cases', icon: FolderOpen },
  { name: 'Investigations', href: '/investigations', icon: Search },
  { name: 'Verdict Lab', href: '/verdict-lab', icon: FlaskConical },
  { name: 'Evaluation', href: '/evaluation', icon: BarChart3 },
]

export function Sidebar() {
  const pathname = usePathname()

  return (
    <div className="w-64 border-r border-slate-800 bg-slate-950 flex flex-col h-full shrink-0">
      <div className="h-16 flex items-center px-6 border-b border-slate-800">
        <Shield className="w-6 h-6 text-cyan-500 mr-3" />
        <span className="font-bold text-slate-100 tracking-tight">AgentShield</span>
        <span className="text-cyan-500 font-bold ml-1">SOC</span>
      </div>
      
      <div className="flex-1 py-6 px-3 space-y-1 overflow-y-auto">
        <div className="text-xs font-semibold text-slate-500 mb-4 px-3 uppercase tracking-wider">Navigation</div>
        {navigation.map((item) => {
          const isActive = pathname === item.href
          return (
            <Link key={item.name} href={item.href} className={cn("flex items-center px-3 py-2 text-sm rounded-md transition-colors", isActive ? "bg-cyan-950/30 text-cyan-400 font-medium" : "text-slate-400 hover:text-slate-200 hover:bg-slate-900")}>
              <item.icon className={cn("w-4 h-4 mr-3", isActive ? "text-cyan-400" : "text-slate-500")} />
              {item.name}
            </Link>
          )
        })}
      </div>
      
      <div className="p-4 border-t border-slate-800">
        <Link href="/settings" className={cn("flex items-center px-3 py-2 text-sm rounded-md transition-colors", pathname === '/settings' ? "bg-cyan-950/30 text-cyan-400 font-medium" : "text-slate-400 hover:text-slate-200 hover:bg-slate-900")}>
          <Settings className="w-4 h-4 mr-3 text-slate-500" />
          Settings
        </Link>
      </div>
    </div>
  )
}
