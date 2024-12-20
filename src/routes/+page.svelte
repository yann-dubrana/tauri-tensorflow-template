<script lang="ts">
    import {fade} from "svelte/transition";
    import {serverHealthStore} from "$lib/health.store.svelte.js";
    import {Card} from "flowbite-svelte";
    import {Activity} from "lucide-svelte";
    import SystemCard from "$lib/components/SystemCard.svelte";
    import CPUCard from "$lib/components/CPUCard.svelte";
    import MemoryCard from "$lib/components/MemoryCard.svelte";
    import GPUCard from "$lib/components/GPUCard.svelte";
    import {
        getSystemInfo,
        getTensorflowInfo,
        type GPUInfo,
        type SystemInfo,
    } from "$lib/client";

    let systemInfo: SystemInfo | undefined = $state(undefined);
    let gpuInfo: GPUInfo | undefined = $state(undefined);


    $effect(() => {
        if (serverHealthStore.isReady) {
            getSystemInfo().then((response) => {
                systemInfo = response.data
            });

            getTensorflowInfo().then((response) => {
                gpuInfo = response.data
            });
        }
    });
</script>


<div class="min-h-screen w-full bg-background p-4 md:p-6 lg:p-8">
    <div class="container mx-auto space-y-8">
        <!-- Header -->
        <div class="flex flex-col gap-2">
            <h1 class="text-3xl font-bold tracking-tight">System Dashboard</h1>
            <p class="text-muted-foreground">Comprehensive system and environment information</p>
        </div>

        <!-- Health Status -->
        <Card>
            <div class="flex flex-row items-center justify-between space-y-0 pb-2">
                <h3 class="text-sm font-medium">System Health</h3>
                <Activity
                        class={serverHealthStore.status === "healthy" ? "text-green-500 animate-pulse" : "text-red-500"}
                        size={16}/>
            </div>
            <div>
                <div class="text-2xl font-bold">{serverHealthStore.status}</div>
            </div>
        </Card>

        {#if serverHealthStore.isReady}
            <!-- Grid Layout -->
            <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-3" transition:fade>
                {#if systemInfo}
                    <SystemCard systemInfo={systemInfo.os} pythonVersion={systemInfo.python_version}/>
                    <CPUCard cpuInfo={systemInfo.cpu}/>
                    <MemoryCard memoryInfo={systemInfo.memory}/>
                {/if}

                {#if gpuInfo}
                    <GPUCard {gpuInfo}/>
                {/if}

            </div>
        {/if}
    </div>
</div>

