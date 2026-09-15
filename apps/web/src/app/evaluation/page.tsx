import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"

export default function Evaluation() {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-semibold text-slate-100 tracking-tight">Evaluation Dashboard</h1>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card>
          <CardContent className="p-4">
            <div className="text-xs text-slate-500 uppercase tracking-wider mb-1">Precision</div>
            <div className="text-xl text-slate-400">—</div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="p-4">
            <div className="text-xs text-slate-500 uppercase tracking-wider mb-1">Recall</div>
            <div className="text-xl text-slate-400">—</div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="p-4">
            <div className="text-xs text-slate-500 uppercase tracking-wider mb-1">F1 Score</div>
            <div className="text-xl text-slate-400">—</div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="p-4">
            <div className="text-xs text-slate-500 uppercase tracking-wider mb-1">Accuracy</div>
            <div className="text-xl text-slate-400">—</div>
          </CardContent>
        </Card>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <Card>
          <CardHeader>
            <CardTitle className="text-slate-300 text-sm uppercase tracking-wider">Confusion Matrix</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="overflow-x-auto">
              <table className="w-full text-sm text-center border-collapse">
                <thead>
                  <tr>
                    <th className="p-2 border border-slate-800 bg-slate-900/50"></th>
                    <th colSpan={3} className="p-2 border border-slate-800 bg-slate-900/50 text-slate-400 font-medium">Predicted</th>
                  </tr>
                  <tr>
                    <th className="p-2 border border-slate-800 bg-slate-900/50 text-slate-400 font-medium text-left">Actual</th>
                    <th className="p-2 border border-slate-800 text-slate-500 font-normal">Malicious</th>
                    <th className="p-2 border border-slate-800 text-slate-500 font-normal">Benign</th>
                    <th className="p-2 border border-slate-800 text-slate-500 font-normal">Unknown</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <th className="p-2 border border-slate-800 text-slate-500 font-normal text-left bg-slate-900/20">Malicious</th>
                    <td className="p-2 border border-slate-800 text-slate-600">—</td>
                    <td className="p-2 border border-slate-800 text-slate-600">—</td>
                    <td className="p-2 border border-slate-800 text-slate-600">—</td>
                  </tr>
                  <tr>
                    <th className="p-2 border border-slate-800 text-slate-500 font-normal text-left bg-slate-900/20">Benign</th>
                    <td className="p-2 border border-slate-800 text-slate-600">—</td>
                    <td className="p-2 border border-slate-800 text-slate-600">—</td>
                    <td className="p-2 border border-slate-800 text-slate-600">—</td>
                  </tr>
                  <tr>
                    <th className="p-2 border border-slate-800 text-slate-500 font-normal text-left bg-slate-900/20">Unknown</th>
                    <td className="p-2 border border-slate-800 text-slate-600">—</td>
                    <td className="p-2 border border-slate-800 text-slate-600">—</td>
                    <td className="p-2 border border-slate-800 text-slate-600">—</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <p className="text-xs text-slate-600 mt-4 text-center">Awaiting evaluation data.</p>
          </CardContent>
        </Card>
        
        <Card>
          <CardHeader>
            <CardTitle className="text-slate-300 text-sm uppercase tracking-wider">Classification Summary</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div className="flex justify-between border-b border-slate-800/50 pb-2">
                <span className="text-slate-400">True Positives (TP)</span>
                <span className="text-slate-600">—</span>
              </div>
              <div className="flex justify-between border-b border-slate-800/50 pb-2">
                <span className="text-slate-400">True Negatives (TN)</span>
                <span className="text-slate-600">—</span>
              </div>
              <div className="flex justify-between border-b border-slate-800/50 pb-2">
                <span className="text-slate-400">False Positives (FP)</span>
                <span className="text-slate-600">—</span>
              </div>
              <div className="flex justify-between border-b border-slate-800/50 pb-2">
                <span className="text-slate-400">False Negatives (FN)</span>
                <span className="text-slate-600">—</span>
              </div>
              <div className="flex justify-between">
                <span className="text-slate-400">Unknown / Unclassified</span>
                <span className="text-slate-600">—</span>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
