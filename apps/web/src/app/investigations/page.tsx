import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"

export default function Investigations() {
  return (
    <div className="space-y-6 h-full flex flex-col">
      <h1 className="text-2xl font-semibold text-slate-100 tracking-tight">Investigations</h1>
      
      <div className="grid grid-cols-12 gap-6 flex-1 min-h-0">
        <Card className="col-span-3">
          <CardHeader className="py-4 px-4 border-b border-slate-800">
            <CardTitle className="text-sm">Cases</CardTitle>
          </CardHeader>
          <CardContent className="p-4 text-sm text-slate-500">
            Select a case to investigate
          </CardContent>
        </Card>
        
        <Card className="col-span-6">
          <CardHeader className="py-4 px-4 border-b border-slate-800">
            <CardTitle className="text-sm">Investigation Workspace</CardTitle>
          </CardHeader>
          <CardContent className="p-8 text-center text-slate-500 flex flex-col items-center justify-center h-full">
            <div className="mb-2">Evidence collection will appear here.</div>
            <p className="text-xs text-slate-600">Awaiting evidence</p>
          </CardContent>
        </Card>
        
        <Card className="col-span-3 bg-slate-900/30">
          <CardHeader className="py-4 px-4 border-b border-slate-800">
            <CardTitle className="text-sm text-cyan-400">AI Assistant</CardTitle>
          </CardHeader>
          <CardContent className="p-4 text-sm text-slate-500">
            Investigation has not started.
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
