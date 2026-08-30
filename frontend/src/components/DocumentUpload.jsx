import { useState } from "react";

const MAX_FILE_SIZE = 10 * 1024 * 1024;

const DocumentUpload = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState("");
  const [isUploading, setIsUploading] = useState(false);

  const handleFileChange = (event) => {
    const file = event.target.files[0];

    setUploadStatus("");

    if (!file) {
      setSelectedFile(null);
      return;
    }

    if (file.size > MAX_FILE_SIZE) {
      setSelectedFile(null);
      setUploadStatus("File size must be 10 MB or less.");
      event.target.value = "";
      return;
    }

    setSelectedFile(file);
  };

  const handleUpload = async (event) => {
    event.preventDefault();

    if (!selectedFile) {
      setUploadStatus("Please select a document.");
      return;
    }

    const form = event.currentTarget;
    const formData = new FormData();

    formData.append("file", selectedFile);

    try {
      setIsUploading(true);
      setUploadStatus("");

      const response = await fetch(
        `${import.meta.env.VITE_API_BASE_URL}/api/documents/upload`,
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Document upload failed");
      }

      setUploadStatus(
        `${data.original_filename} uploaded successfully.`
      );

      setSelectedFile(null);
      form.reset();
    } catch (error) {
      console.error(error);
      setUploadStatus(error.message);
    } finally {
      setIsUploading(false);
    }
  };

  return (
    <section className="upload-card">
      <h2>Upload a document</h2>

      <p>Supported formats: PDF, TXT and Markdown. Maximum size: 10 MB.</p>

      <form onSubmit={handleUpload}>
        <input
          type="file"
          accept=".pdf,.txt,.md"
          onChange={handleFileChange}
          disabled={isUploading}
        />

        {selectedFile && (
          <p className="selected-file">
            Selected: {selectedFile.name}
          </p>
        )}

        <button
          type="submit"
          disabled={!selectedFile || isUploading}
        >
          {isUploading ? "Uploading..." : "Upload document"}
        </button>
      </form>

      {uploadStatus && (
        <p className="upload-status">{uploadStatus}</p>
      )}
    </section>
  );
};

export default DocumentUpload;