import type { Config } from 'tailwindcss';
import flowbitePlugin from 'flowbite/plugin'

export default {
    content: ['./src/**/*.{html,js,svelte,ts}', './node_modules/flowbite-svelte/**/*.{html,js,svelte,ts}'],
    darkMode: 'selector',
    theme: {
        extend: {
            colors: {
                // flowbite-svelte
                primary: {
                    '50': '#f2f7fb',
                    '100': '#e7f0f8',
                    '200': '#d3e2f2',
                    '300': '#b9cfe8',
                    '400': '#9cb6dd',
                    '500': '#839dd1',
                    '600': '#6a7fc1',
                    '700': '#6374ae',
                    '800': '#4a5989',
                    '900': '#414e6e',
                    '950': '#262c40',
                },
                'green': {
                    '50': '#edfee7',
                    '100': '#d7fdca',
                    '200': '#9ff983',
                    '300': '#81f462',
                    '400': '#59e833',
                    '500': '#37ce14',
                    '600': '#25a50b',
                    '700': '#1f7d0e',
                    '800': '#1d6311',
                    '900': '#1b5413',
                    '950': '#082f04',
                },
                'red': {
                    '50': '#fff0f0',
                    '100': '#ffdddd',
                    '200': '#ffc0c0',
                    '300': '#ff9494',
                    '400': '#ff5757',
                    '500': '#ff2323',
                    '600': '#ff0000',
                    '700': '#d70000',
                    '800': '#b10303',
                    '900': '#920a0a',
                    '950': '#500000',
                },
                'gray': {
                    '50': '#f6f6f6',
                    '100': '#e7e7e7',
                    '200': '#d1d1d1',
                    '300': '#b0b0b0',
                    '400': '#808080',
                    '500': '#6d6d6d',
                    '600': '#5d5d5d',
                    '700': '#4f4f4f',
                    '800': '#454545',
                    '900': '#3d3d3d',
                    '950': '#262626',
                },

            }
        }
    },

    plugins: [flowbitePlugin]
} as Config;
