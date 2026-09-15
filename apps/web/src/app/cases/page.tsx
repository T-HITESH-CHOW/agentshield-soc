import { Card } from "@/components/ui/card"

export default function Cases() {
  return (
    <div className="space-y-6 h-full flex flex-col">
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-semibold text-slate-100 tracking-tight">Cases</h1>
      </div>
      
      <Card className="flex-1 flex items-center justify-center text-slate-500">
        <div className="text-center">
          <div className="text-lg mb-2">No cases yet</div>
          <p className="text-sm">Cases created from alerts will appear here.</p>
        </div>
      </Card>
    </div>
  )
}
