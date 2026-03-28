const browserApiBase =
  process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

const serverApiBase =
  process.env.INTERNAL_API_URL ||
  process.env.NEXT_PUBLIC_API_URL ||
  "http://backend:8000";

export function getApiBaseUrl() {
  return typeof window === "undefined" ? serverApiBase : browserApiBase;
}

export function apiUrl(path: string) {
  const baseUrl = getApiBaseUrl().replace(/\/$/, "");
  const normalizedPath = path.startsWith("/") ? path : `/${path}`;
  return `${baseUrl}${normalizedPath}`;
}
