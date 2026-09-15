import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Brain, User } from "lucide-react"

export default function VerdictLab() {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-semibold text-slate-100 tracking-tight">Verdict Lab</h1>
          <p className="text-sm text-slate-500 mt-1">Evidence-first analyst workspace</p>
        </div>
      </div>
      
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        
        {/* LEFT COLUMN: SYSTEM VS ANALYST */}
        <div className="space-y-6">
          <Card className="border-cyan-900/50 bg-cyan-950/10">
            <CardHeader className="border-b border-cyan-900/30 pb-4">
              <div className="flex items-center justify-between">
                <CardTitle className="text-cyan-400 flex items-center text-sm uppercase tracking-wider">
                  <Brain className="w-4 h-4 mr-2" /> System Prediction
                </CardTitle>
                <Badge variant="outline" className="border-cyan-800 text-cyan-500">Auto</Badge>
              </div>
            </CardHeader>
            <CardContent className="pt-6">
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <div className="text-xs text-slate-500 mb-1">Proposed Verdict</div>
                  <div className="text-lg font-medium text-slate-300">Awaiting analysis</div>
                </div>
                <div>
                  <div className="text-xs text-slate-500 mb-1">Confidence</div>
                  <div className="text-lg font-medium text-slate-500">—</div>
                </div>
              </div>
            </CardContent>
          </Card>
          
          <Card className="border-amber-900/50 bg-amber-950/10">
             <CardHeader className="border-b border-amber-900/30 pb-4">
              <div className="flex items-center justify-between">
                <CardTitle className="text-amber-400 flex items-center text-sm uppercase tracking-wider">
                  <User className="w-4 h-4 mr-2" /> Analyst Ground Truth
                </CardTitle>
                <Badge variant="outline" className="border-amber-800 text-amber-500">Manual</Badge>
              </div>
            </CardHeader>
            <CardContent className="pt-6">
              <div className="text-slate-500">Not labeled.</div>
            </CardContent>
          </Card>
          
          <Card>
             <CardHeader className="border-b border-slate-800 pb-4">
              <CardTitle className="text-slate-300 flex items-center text-sm uppercase tracking-wider">
                 Evaluation Result
              </CardTitle>
            </CardHeader>
            <CardContent className="pt-6">
              <div className="text-slate-500">Not evaluated.</div>
            </CardContent>
          </Card>
        </div>
        
        {/* RIGHT COLUMN: EVIDENCE & AI */}
        <div className="space-y-6">
          <Card>
             <CardHeader className="border-b border-slate-800 pb-4">
              <CardTitle className="text-slate-300 flex items-center text-sm uppercase tracking-wider">
                 Evidence
              </CardTitle>
            </CardHeader>
            <CardContent className="pt-6">
              <div className="text-slate-500 text-sm">No evidence collected.</div>
            </CardContent>
          </Card>
          
          <Card>
             <CardHeader className="border-b border-slate-800 pb-4">
              <CardTitle className="text-slate-300 flex items-center text-sm uppercase tracking-wider">
                 Counter-Evidence
              </CardTitle>
            </CardHeader>
            <CardContent className="pt-6">
              <div className="text-slate-500 text-sm">No counter-evidence collected.</div>
            </CardContent>
          </Card>
          
          <Card className="bg-slate-900/30">
             <CardHeader className="border-b border-slate-800 pb-4">
              <CardTitle className="text-slate-300 flex items-center text-sm uppercase tracking-wider">
                 AI Investigation
              </CardTitle>
            </CardHeader>
            <CardContent className="pt-6">
              <div className="text-slate-500 text-sm">Investigation has not started.</div>
            </CardContent>
          </Card>
        </div>

      </div>
    </div>
  )
}
