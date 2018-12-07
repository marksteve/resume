workflow "Render PDF" {
  on = "push"
  resolves = ["Markdown to PDF", "Upload to GCS"]
}

action "Markdown to PDF" {
  uses = "./md2pdf"
}

action "Auth with Google Cloud" {
  uses = "actions/gcloud/auth@8ec8bfa"
  needs = ["Markdown to PDF"]
  secrets = ["GCLOUD_AUTH"]
}

action "Upload to GCS" {
  uses = "actions/gcloud/cli@8ec8bfa"
  runs = "gsutil"
  args = "cp resume.pdf gs://marksteve/resume.pdf"
  needs = ["Auth with Google Cloud"]
}
