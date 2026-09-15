import { Search, Bell, User } from "lucide-react"

export function TopBar() {
  return (
    <header className="h-16 border-b border-slate-800 bg-slate-950 flex items-center justify-between px-6 shrink-0">
      <div className="flex items-center">
        <div className="flex items-center text-xs px-2 py-1 bg-green-950/30 text-green-400 border border-green-900 rounded-full">
          <span className="w-2 h-2 rounded-full bg-green-500 mr-2"></span>
          Environment: Operational
        </div>
      </div>
      
      <div className="flex items-center space-x-4">
        <div className="relative group">
          <Search className="w-4 h-4 text-slate-500 absolute left-3 top-1/2 -translate-y-1/2 group-focus-within:text-cyan-400" />
          <input type="text" placeholder="Search across SOC..." className="w-64 bg-slate-900 border border-slate-800 text-sm text-slate-200 rounded-md py-1.5 pl-9 pr-3 focus:outline-none focus:border-cyan-700 focus:ring-1 focus:ring-cyan-700 placeholder:text-slate-600" />
        </div>
        
        <button className="text-slate-500 hover:text-slate-300 relative">
          <Bell className="w-5 h-5" />
          <span className="absolute top-0 right-0 w-2 h-2 bg-cyan-500 rounded-full"></span>
        </button>
        
        <div className="w-8 h-8 rounded-full bg-slate-800 flex items-center justify-center border border-slate-700 text-slate-400">
          <User className="w-4 h-4" />
        </div>
      </div>
    </header>
  )
}
