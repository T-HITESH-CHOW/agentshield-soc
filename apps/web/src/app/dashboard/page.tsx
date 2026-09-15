import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Activity, ShieldAlert, FileSearch, Target } from "lucide-react"

export default function Dashboard() {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-semibold text-slate-100 tracking-tight">SOC Dashboard</h1>
      
      {/* 1. SECURITY OVERVIEW */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <MetricCard title="Active Alerts" value="Awaiting telemetry" icon={ShieldAlert} />
        <MetricCard title="Open Cases" value="Awaiting telemetry" icon={FileSearch} />
        <MetricCard title="Investigations" value="Awaiting telemetry" icon={Activity} />
        <MetricCard title="Critical Risk" value="Awaiting evidence" icon={Target} />
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* 2. ATTACK PATH / ENVIRONMENT GRAPH */}
        <Card className="col-span-2 min-h-[400px] flex flex-col">
          <CardHeader>
            <CardTitle className="text-slate-300 flex items-center">Attack Path Visualization</CardTitle>
          </CardHeader>
          <CardContent className="flex-1 flex items-center justify-center border-t border-slate-800/50 mt-2">
            <div className="text-slate-500 flex flex-col items-center">
              <div className="w-16 h-16 rounded-full border-2 border-dashed border-slate-700 flex items-center justify-center mb-4">
                <Target className="w-6 h-6 text-slate-600" />
              </div>
              <p>Awaiting telemetry</p>
              <p className="text-xs text-slate-600 mt-2">Environment graph will appear here</p>
            </div>
          </CardContent>
        </Card>

        {/* 3. RISK OVERVIEW */}
        <Card className="flex flex-col">
          <CardHeader>
            <CardTitle className="text-slate-300">Risk Overview</CardTitle>
          </CardHeader>
          <CardContent className="flex-1 flex flex-col items-center justify-center border-t border-slate-800/50 mt-2 py-10">
            <div className="relative w-48 h-48 rounded-full border-8 border-slate-900 flex items-center justify-center shadow-inner">
               <div className="absolute inset-0 rounded-full border-[10px] border-cyan-950/20 border-t-cyan-500/20" style={{ transform: 'rotate(-45deg)' }}></div>
               <div className="text-center">
                 <div className="text-sm text-slate-500 mb-1">Risk Score</div>
                 <div className="text-lg font-medium text-slate-400">Awaiting evidence</div>
               </div>
            </div>
          </CardContent>
        </Card>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* 4. ACTIVE THREATS */}
        <Card className="col-span-2">
          <CardHeader>
            <CardTitle className="text-slate-300">Active Threats</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="h-48 flex items-center justify-center text-slate-500 text-sm border border-dashed border-slate-800 rounded-lg">
              No active threats
            </div>
          </CardContent>
        </Card>

        <div className="space-y-6">
          {/* 5. INVESTIGATION ACTIVITY */}
          <Card>
            <CardHeader>
              <CardTitle className="text-slate-300">Investigation Activity</CardTitle>
            </CardHeader>
            <CardContent>
               <div className="h-32 flex items-center justify-center text-slate-500 text-sm border border-dashed border-slate-800 rounded-lg">
                No recent activity
              </div>
            </CardContent>
          </Card>
          
          {/* 6. SYSTEM HEALTH */}
          <Card>
            <CardHeader>
              <CardTitle className="text-slate-300">System Health</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <HealthRow name="Ingestion" status="Not connected" />
              <HealthRow name="Detection" status="Not configured" />
              <HealthRow name="AI Gateway" status="Not connected" />
              <HealthRow name="Database" status="Not connected" />
              <HealthRow name="Threat Intelligence" status="Not configured" />
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  )
}

function MetricCard({ title, value, icon: Icon }: { title: string, value: string, icon: React.ElementType }) {
  return (
    <Card>
      <CardContent className="p-5 flex items-center justify-between">
        <div>
          <p className="text-xs font-medium text-slate-500 uppercase tracking-wider">{title}</p>
          <h4 className="text-xl font-semibold text-slate-200 mt-1">{value}</h4>
        </div>
        <div className="w-10 h-10 rounded-full bg-slate-900 flex items-center justify-center text-slate-500">
          <Icon className="w-5 h-5" />
        </div>
      </CardContent>
    </Card>
  )
}

function HealthRow({ name, status }: { name: string, status: string }) {
  return (
    <div className="flex items-center justify-between text-sm">
      <span className="text-slate-400">{name}</span>
      <span className="text-slate-500 text-xs px-2 py-0.5 bg-slate-900 rounded">{status}</span>
    </div>
  )
}
