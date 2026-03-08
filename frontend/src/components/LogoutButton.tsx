"use client";
import { useRouter } from "next/navigation";
import { LogOut } from "lucide-react";

export default function LogoutButton() {
  const router = useRouter();

  const handleLogout = () => {
    localStorage.removeItem("token");
    document.cookie = "token=; Max-Age=0; path=/";
    router.push("/login");
  };

  return (
    <button
      onClick={handleLogout}
      className="p-2 text-red-500 hover:bg-red-100 rounded"
      title="Log out from your account"
    >
      <LogOut size={20} />
    </button>
  );
}