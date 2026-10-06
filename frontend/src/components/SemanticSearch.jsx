import { useState } from "react";

const SemanticSearch = () => {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [isSearching, setIsSearching] = useState(false);
  const [error, setError] = useState("");
  
  const handleChange = (e)=>{
    setQuery(e.target.value)
  }
  const handleSubmit = async (e)=>{
    e.preventDefault()
    const trimmedQuery = query.trim();

    if (!trimmedQuery) {
        return;
    }
    setError('')
    setResults([])
    setIsSearching(true)
    try {
        const response = await fetch(
            `${import.meta.env.VITE_API_BASE_URL}/api/search/semantic`,
            {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                query: trimmedQuery,
                number_of_results: 1,
            }),
            }
        );
        const data = await response.json();
        if (!response.ok) {
            throw new Error(data.detail || "Search failed");
        }
        setResults(data.results);
    }catch(error){
        setError(error.message)
    }finally{
        setIsSearching(false);
    }
  }
  return (
    <section className="search-card">
      <h2>Search documents</h2>
      <p>Find relevant information from your uploaded documents.</p>
      <form onSubmit={handleSubmit}>
        <input type="search" value={query} placeholder="input search" disabled={isSearching} onChange={handleChange} />
        <button 
            type="submit"
            disabled={query.trim() === "" || isSearching}
        >{isSearching ? "Searching..." : "Search"}</button>
      </form>
      {error && (<p className="search-error">{error}</p>)}
      {results.length > 0 && (
        <div className="search-results">
                <h3>Search results</h3>

                {results.map((result) => (
                <article
                    className="search-result"
                    key={result.metadata.document_id}
                >
                    <p>{result.content}</p>

                    <small>
                    Source: {result.metadata.source} · Chunk:{" "}
                    {result.metadata.chunk_index}
                    </small>
                </article>
                ))}
        </div>
        )}
    </section>
  );
};

export default SemanticSearch;