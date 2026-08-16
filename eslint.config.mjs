import next from 'eslint-config-next/core-web-vitals';

const eslintConfig = [
  { ignores: ['.next/**', 'node_modules/**', 'cursos/**', '.agents/**', 'public/**'] },
  ...(Array.isArray(next) ? next : [next]),
];

export default eslintConfig;
