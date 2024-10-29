/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    './templates/**/*.html',
    './*/templates/**/*.html',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {
      colors: {
        // Light Mode Colors
        primary: '#10B981',         // Emerald
        background: '#F9FAFB',      // Off White
        secondary: '#E5E7EB',       // Light Gray
        accent: '#6366F1',          // Indigo
        text: '#111827',            // Almost Black
        
        // Dark Mode Colors
        dark: {
          primary: '#34D399',       // Light Emerald
          background: '#0F172A',    // Deep Blue-Black
          secondary: '#1F2937',     // Dark Gray
          accent: '#818CF8',        // Light Indigo
          text: '#F3F4F6'           // Light Gray
        }
      }
    }
  },
  plugins: [
    require('flowbite/plugin'),
    require('daisyui')
  ],
  daisyui: {
    themes: [
      {
        light: {
          primary: '#10B981',
          background: '#F9FAFB',
          secondary: '#E5E7EB',
          accent: '#6366F1',
          text: '#111827',
        },
        dark: {
          primary: '#34D399',
          background: '#0F172A',
          secondary: '#1F2937',
          accent: '#818CF8',
          text: '#F3F4F6',
        }
      }
    ]
  }
};
