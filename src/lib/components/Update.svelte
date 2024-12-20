<script lang="ts">
    import {check, type Update} from '@tauri-apps/plugin-updater';
    import {relaunch} from '@tauri-apps/plugin-process';
    import {onMount} from "svelte";
    import {Button, Progressbar, Toast} from "flowbite-svelte";
    import {ArrowBigDownDash} from "lucide-svelte";

    let toastStatus = $state(false);
    let update: Update | null = $state(null);

    let contentLength: number | undefined = $state(0);
    let downloaded = $state(0);

    let progress = $derived.by(() => {
        if (contentLength === 0 || !contentLength) {
            return 0;
        }
        return downloaded / contentLength * 100;
    });

    onMount(() => {
        checkForUpdates();
    })

    async function checkForUpdates() {
        update = await check();
        toastStatus = (update !== null);
    }

    async function updateApp() {

        if (!update) {
            return;
        }

        await update.downloadAndInstall((event) => {
            switch (event.event) {
                case 'Started':
                    contentLength = event.data.contentLength;
                    break;
                case 'Progress':
                    downloaded += event.data.chunkLength;
                    break;
                case 'Finished':
                    break;
            }
        });

        await relaunch();

    }

    $effect(() => {
        if (!toastStatus) {
            update = null;
        }
    });

</script>

{#if update}
    <Toast dismissable position="bottom-right" toastStatus={toastStatus}>
        {#snippet icon()}
            <ArrowBigDownDash class="w-6 h-6"/>
        {/snippet}

        <span class="font-semibold text-gray-900 dark:text-white">Mise à jour disponible</span>
        <div class="mt-3">
            <div class="mb-2 text-sm font-normal">Version {update.version} disponible pour téléchargement.
            </div>
            {#if downloaded > 0}
                <Progressbar progress={progress} class="my-4"/>
            {/if}

            <div class="grid grid-cols-2 gap-2">
                <Button size="xs" class="w-full" onclick={updateApp}>Mettre à jour</Button>
                <Button size="xs" class="w-full" color="dark" onclick={()=>{update = null}}>Pas maintenant</Button>
            </div>
        </div>
    </Toast>
{/if}
