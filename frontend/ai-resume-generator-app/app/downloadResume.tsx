"use client"

import { Button } from "@/components/ui/button"
import { Card } from "@/components/ui/card"
import { CheckCircle2, Download, FileText } from "lucide-react"
import { jsPDF } from 'jspdf';

export default function DownloadResume({resume} : any) {
  const handleDownload = () => {

    const doc = new jsPDF()
    doc.text(resume, 10, 10)
    doc.setFont("helvetica", "normal");
    doc.setFontSize(11);
    doc.save("Optimized_Resume.pdf")
  }

  return (
    <main className="min-h-screen flex items-center justify-center p-4 bg-gradient-to-br from-background via-background to-muted">
      <Card className="max-w-lg w-full p-8 md:p-12 text-center space-y-6 border-border/50 shadow-2xl">
        <div className="flex justify-center">
          <div className="relative">
            <div className="absolute inset-0 bg-primary/20 blur-2xl rounded-full" />
            <div className="relative bg-primary/10 p-4 rounded-full">
              <CheckCircle2 className="w-16 h-16 text-primary" />
            </div>
          </div>
        </div>

        <div className="space-y-3">
          <h1 className="text-3xl md:text-4xl font-bold text-foreground text-balance">
            Your Resume Has Been Generated!
          </h1>
          <p className="text-muted-foreground text-lg text-pretty leading-relaxed">
            Your professional resume is ready to download. It has been formatted and optimized for success.
          </p>
        </div>

        <div className="pt-4 space-y-3">
          <Button onClick={handleDownload} size="lg" className="w-full text-base font-semibold gap-2 h-12">
            <Download className="w-5 h-5" />
            Download Resume
          </Button>

          <div className="flex items-center justify-center gap-2 text-sm text-muted-foreground">
            <FileText className="w-4 h-4" />
            <span>PDF format • Ready to share</span>
          </div>
        </div>

        <div className="pt-6 border-t border-border/50">
          <p className="text-xs text-muted-foreground">Your resume has been securely generated and is ready for use</p>
        </div>
      </Card>
    </main>
  )
}
