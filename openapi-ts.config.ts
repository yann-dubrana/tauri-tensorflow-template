import { defineConfig } from '@hey-api/openapi-ts';

export default defineConfig({
    client: '@hey-api/client-fetch',
    input: 'http://localhost:63421/openapi.json',
    output: 'src/lib/client'
});
