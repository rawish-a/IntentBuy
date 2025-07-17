import React from 'react';
import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';

// Validation schema
const schema = yup.object().shape({
  email: yup.string().email('Invalid email').required('Email is required'),
  password: yup.string().required('Password is required'),
});

export default function LoginForm({ onSubmit }) {
  const { register, handleSubmit, formState: { errors, isSubmitting } } = useForm({
    resolver: yupResolver(schema)
  });

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      <div>
        <label>Email:</label>
        <input {...register('email')} className="border p-2 w-full" />
        <p className="text-red-500 text-sm">{errors.email?.message}</p>
      </div>

      <div>
        <label>Password:</label>
        <input type="password" {...register('password')} className="border p-2 w-full" />
        <p className="text-red-500 text-sm">{errors.password?.message}</p>
      </div>

      <button type="submit" disabled={isSubmitting} className="bg-green-500 text-white px-4 py-2 rounded">
        {isSubmitting ? 'Logging in...' : 'Login'}
      </button>
    </form>
  );
}
