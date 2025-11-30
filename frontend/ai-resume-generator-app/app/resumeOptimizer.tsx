'use client'

import { useEffect, useState } from 'react'
import { Card } from '@/components/ui/card'
import { Label } from '@/components/ui/label'
import { Textarea } from '@/components/ui/textarea'
import { Button } from '@/components/ui/button'
import { FileText, Upload, Sparkles, ArrowRight } from 'lucide-react'
import  FileUpload  from './file-upload'
import  DownloadResume from './downloadResume'
import axios from 'axios'

export function ResumeOptimizer() {
  const [jobDescription, setJobDescription] = useState('')
  const [uploadedFile, setUploadedFile] = useState<File | null>(null)
  const [isGenerating, setIsGenerating] = useState(false)
  const [backendEndpoint, setBackendEndpoint] = useState('http://127.0.0.1:5000')
  const [isGenerated, setIsGenerated] = useState(false)
  const [generatedResume, setGeneratedResume] = useState("")

  const handleGenerate = async () => {
    if (!jobDescription.trim() || !uploadedFile) {
      return
    }
    
    setIsGenerating(true)
    await new Promise(resolve => setTimeout(resolve, 2000))

    if(jobDescription.trim().length > 0 && uploadedFile !== null){
      await handleHttpRequest()
    }
    
  }
  const canGenerate = jobDescription.trim().length > 0 && uploadedFile !== null

  const handleHttpRequest = async()=>{
    const formData = new FormData()
    formData.append('job_description', jobDescription)
    if(uploadedFile!=null){
      formData.append('resume', uploadedFile)
    }
    const response = await axios.post(`${backendEndpoint}/optimizer/optimize`, formData)
    setGeneratedResume(response.data)
  }

  useEffect(()=>{
    if(generatedResume!==''){
      setIsGenerating(false)
      setIsGenerated(true)
      console.log(generatedResume)
    }

  },[generatedResume])

  return (
    !isGenerated ?
    <div className="container mx-auto px-4 py-12 md:py-20 max-w-5xl">
      {/* Header */}
      <div className="text-center mb-12 md:mb-16">
        <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-primary/10 text-primary text-sm font-medium mb-6">
          <Sparkles className="w-4 h-4" />
          <span>AI-Powered Resume Optimization</span>
        </div>
        <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold tracking-tight mb-4 text-balance">
          Tailor Your Resume to Any Job
        </h1>
        <p className="text-lg md:text-xl text-muted-foreground max-w-2xl mx-auto text-pretty">
          Upload your resume and paste the job description. Our AI will optimize your resume to match the role perfectly.
        </p>
      </div>

      {/* Main Content */}
      <div className="grid md:grid-cols-2 gap-6 mb-8">
        {/* Job Description Card */}
        <Card className="p-6 md:p-8 border-2 hover:border-primary/50 transition-colors">
          <div className="flex items-center gap-3 mb-6">
            <div className="w-10 h-10 rounded-lg bg-primary/10 flex items-center justify-center">
              <FileText className="w-5 h-5 text-primary" />
            </div>
            <div>
              <h2 className="text-xl font-semibold">Job Description</h2>
              <p className="text-sm text-muted-foreground">Paste the full job posting</p>
            </div>
          </div>
          
          <div className="space-y-2">
            <Label htmlFor="job-description" className="text-sm font-medium">
              Job Requirements & Description
            </Label>
            <Textarea
              id="job-description"
              placeholder="Paste the complete job description here, including requirements, responsibilities, and qualifications..."
              value={jobDescription}
              onChange={(e) => setJobDescription(e.target.value)}
              className="min-h-[300px] resize-none text-sm leading-relaxed"
            />
            <p className="text-xs text-muted-foreground">
              {jobDescription.length} characters
            </p>
          </div>
        </Card>

        {/* Resume Upload Card */}
        <Card className="p-6 md:p-8 border-2 hover:border-primary/50 transition-colors">
          <div className="flex items-center gap-3 mb-6">
            <div className="w-10 h-10 rounded-lg bg-accent/10 flex items-center justify-center">
              <Upload className="w-5 h-5 text-accent" />
            </div>
            <div>
              <h2 className="text-xl font-semibold">Your Resume</h2>
              <p className="text-sm text-muted-foreground">Upload your current resume</p>
            </div>
          </div>
          
          <FileUpload 
            onFileSelect={setUploadedFile}
            selectedFile={uploadedFile}
          />
        </Card>
      </div>

      {/* Generate Button */}
      <div className="flex flex-col items-center gap-4">
        <Button
          size="lg"
          className="w-full md:w-auto px-8 py-6 text-lg font-semibold shadow-lg hover:shadow-xl transition-all"
          onClick={handleGenerate}
          disabled={!canGenerate || isGenerating}
        >
          {isGenerating ? (
            <>
              <div className="w-5 h-5 border-2 border-primary-foreground/30 border-t-primary-foreground rounded-full animate-spin mr-2" />
              Generating Your Resume...
            </>
          ) : (
            <>
              <Sparkles className="w-5 h-5 mr-2" />
              Generate Optimized Resume
              <ArrowRight className="w-5 h-5 ml-2" />
            </>
          )}
        </Button>
        
        {!canGenerate && (
          <p className="text-sm text-muted-foreground">
            Please provide both a job description and upload your resume to continue
          </p>
        )}
      </div>

      {/* Features */}
      <div className="mt-16 pt-16 border-t">
        <div className="grid md:grid-cols-3 gap-8">
          <div className="text-center">
            <div className="w-12 h-12 rounded-full bg-primary/10 flex items-center justify-center mx-auto mb-4">
              <Sparkles className="w-6 h-6 text-primary" />
            </div>
            <h3 className="font-semibold mb-2">AI-Powered Matching</h3>
            <p className="text-sm text-muted-foreground leading-relaxed">
              Automatically highlights relevant skills and experiences that match the job requirements
            </p>
          </div>
          <div className="text-center">
            <div className="w-12 h-12 rounded-full bg-accent/10 flex items-center justify-center mx-auto mb-4">
              <FileText className="w-6 h-6 text-accent" />
            </div>
            <h3 className="font-semibold mb-2">ATS-Friendly Format</h3>
            <p className="text-sm text-muted-foreground leading-relaxed">
              Ensures your resume passes applicant tracking systems with optimized formatting
            </p>
          </div>
          <div className="text-center">
            <div className="w-12 h-12 rounded-full bg-primary/10 flex items-center justify-center mx-auto mb-4">
              <Upload className="w-6 h-6 text-primary" />
            </div>
            <h3 className="font-semibold mb-2">Instant Generation</h3>
            <p className="text-sm text-muted-foreground leading-relaxed">
              Get your tailored resume in seconds, ready to download and submit
            </p>
          </div>
        </div>
      </div>
    </div>
    : 
    <DownloadResume />
  )
}
