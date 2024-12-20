<script lang="ts">
    import {HardDriveIcon} from "lucide-svelte";
    import {Card} from "flowbite-svelte";
    import type {GPUInfo} from "$lib/client";

    let {gpuInfo}: { gpuInfo: GPUInfo } = $props();
</script>

<Card>
    <div class="flex flex-row items-center justify-between space-y-0 pb-2">
        <h3 class="text-sm font-medium">GPU Information</h3>
        <HardDriveIcon size={16}/>
    </div>
    <div class="space-y-3">
        <div class="space-y-1">
            <p class="text-sm font-medium">Version</p>
            <p class="text-sm text-muted-foreground">{gpuInfo.version}</p>
        </div>
        <div class="space-y-1">
            <p class="text-sm font-medium">GPU Devices</p>
            {#if gpuInfo.gpu_devices}
                {#each gpuInfo.gpu_devices as device}
                    <p class="text-sm text-muted-foreground">{device}</p>
                {/each}
            {:else}
                <p class="text-sm text-muted-foreground">No GPU devices detected</p>
            {/if}
        </div>
        <div class="space-y-1">
            <p class="text-sm font-medium">Features</p>
            <p class="text-sm text-muted-foreground">
                CUDA: {gpuInfo.built_with_cuda ? "Yes" : "No"}
                <br/>
                Eager Execution: {gpuInfo.eager_execution ? "Enabled" : "Disabled"}
            </p>
        </div>
    </div>
</Card>
