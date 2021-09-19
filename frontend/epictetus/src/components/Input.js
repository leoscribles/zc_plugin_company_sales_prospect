import React from 'react';
import '../App.css'

export default function Input({ title, label, placeholder, disabled = false, onChange, id, required, value }) {
    return (
        <div className="mb-6">
            <label className=" mb-2 block font-bold text-base" htmlFor={title}>
                {label}
            </label>
            <input value={value} onChange={onChange} required className="border border-gray-500 outline-none placeholder-gray-400 rounded-sm h-12  w-full px-5 focus:border-primary" id={id} type="text" placeholder={placeholder} disabled={disabled} />
        </div>
    )
}
