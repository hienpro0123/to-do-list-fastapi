import { useFormStatus } from "react-dom"

export default function SubmitButton({ disabled }: { disabled?: boolean }) {
    const {pending} = useFormStatus()
    const isDisabled = disabled || pending
  return (
    <button disabled={isDisabled} className="px-2 py-1 bg-teal-600 text-white rounded-md w-full mt-4 disabled:bg-gray-400" >
      {
        isDisabled ? "Saving..." : "Save"
      }
    </button >
  )
}

