import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"

export default function Settings() {
  const sections = [
    "General", "AI Provider", "Integrations", "Detection", "Notifications", "Security"
  ]

  return (
    <div className="space-y-6 h-full">
      <h1 className="text-2xl font-semibold text-slate-100 tracking-tight">Settings</h1>
      
      <div className="grid grid-cols-12 gap-6 items-start">
        <div className="col-span-3 space-y-1">
          {sections.map(s => (
            <button key={s} className="w-full text-left px-4 py-2 rounded-md text-sm text-slate-400 hover:text-slate-200 hover:bg-slate-900 transition-colors">
              {s}
            </button>
          ))}
        </div>
        
        <div className="col-span-9">
          <Card>
            <CardHeader>
              <CardTitle className="text-lg">Configuration</CardTitle>
            </CardHeader>
            <CardContent className="h-64 flex items-center justify-center text-slate-500">
              Settings UI placeholders only.
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  )
}
