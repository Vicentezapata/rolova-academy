/** @type {import('next').NextConfig} */
const nextConfig = {
  outputFileTracingIncludes: {
    '/api/**/*': ['./cursos/**/*'],
  },
};

export default nextConfig;
