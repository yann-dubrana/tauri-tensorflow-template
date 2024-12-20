<script lang="ts">
    import { MemoryStick } from "lucide-svelte";
    import { Card,Progressbar  } from "flowbite-svelte";
    import type {MemoryInfo} from "$lib/client";

    let { memoryInfo }: { memoryInfo: MemoryInfo } = $props();

    const toGB = (bytes: number) => (bytes / 1024).toFixed(2);
</script>

<Card>
    <div class="flex flex-row items-center justify-between space-y-0 pb-2">
        <h3 class="text-sm font-medium">Memory Usage</h3>
        <MemoryStick size={16} />
    </div>
    <div class="space-y-3">
        <div class="space-y-2">
            <p class="text-sm font-medium">Memory Usage</p>
            <Progressbar  progress={memoryInfo.percentage} />
            <p class="text-xs text-muted-foreground">{memoryInfo.percentage}% used</p>
        </div>
        <div class="space-y-1">
            <p class="text-sm font-medium">Details</p>
            <p class="text-sm text-muted-foreground">
                Total: {toGB(memoryInfo.total)}GB
                <br />
                Used: {toGB(memoryInfo.used)}GB
                <br />
                Available: {toGB(memoryInfo.available)}GB
            </p>
        </div>
    </div>
</Card>
