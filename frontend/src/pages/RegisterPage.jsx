import React from 'react';
import RegisterForm from '../components/RegisterForm';
import { registerUser } from '../api/auth';

export default function RegisterPage() {
  const handleRegister = async (formData) => {
    try {
      const data = await registerUser(formData);
      alert('Registered! You can now log in.');
      console.log(data);
    } catch (err) {
      alert(err.message);
    }
  };

  return (
    <div className="max-w-md mx-auto mt-10">
      <h1 className="text-xl font-bold mb-4">Register</h1>
      <RegisterForm onSubmit={handleRegister} />
    </div>
  );
}
