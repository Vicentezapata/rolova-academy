/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    outputFileTracingIncludes: {
      '/api/**/*': ['./cursos/**/*'],
    },
  },
};

export default nextConfig;
