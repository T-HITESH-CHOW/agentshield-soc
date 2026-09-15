import { Card } from "@/components/ui/card"
import { Search, Filter } from "lucide-react"

export default function Alerts() {
  return (
    <div className="space-y-6 h-full flex flex-col">
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-semibold text-slate-100 tracking-tight">Alerts</h1>
        <div className="flex space-x-3">
          <div className="relative">
            <Search className="w-4 h-4 text-slate-500 absolute left-3 top-1/2 -translate-y-1/2" />
            <input type="text" placeholder="Search alerts..." className="w-64 bg-slate-950 border border-slate-800 text-sm text-slate-200 rounded-md py-1.5 pl-9 pr-3 focus:outline-none focus:border-cyan-700" />
          </div>
          <button className="flex items-center px-3 py-1.5 bg-slate-900 border border-slate-800 text-slate-300 text-sm rounded-md hover:bg-slate-800 transition-colors">
            <Filter className="w-4 h-4 mr-2" /> Filters
          </button>
        </div>
      </div>
      
      <Card className="flex-1">
        <div className="w-full overflow-auto">
          <table className="w-full text-sm text-left">
            <thead className="text-xs text-slate-500 uppercase bg-slate-900/50 border-b border-slate-800">
              <tr>
                <th className="px-6 py-3 font-medium">Severity</th>
                <th className="px-6 py-3 font-medium">Alert</th>
                <th className="px-6 py-3 font-medium">Source</th>
                <th className="px-6 py-3 font-medium">Asset</th>
                <th className="px-6 py-3 font-medium">MITRE</th>
                <th className="px-6 py-3 font-medium">Risk</th>
                <th className="px-6 py-3 font-medium">Status</th>
                <th className="px-6 py-3 font-medium">Created</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td colSpan={8} className="px-6 py-12 text-center text-slate-500 border-b border-slate-800/50">
                  No alerts yet
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </Card>
    </div>
  )
}
