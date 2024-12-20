<script lang="ts">
    import {Cpu} from "lucide-svelte";
    import {Card} from "flowbite-svelte";
    import type {CPUInfo} from "$lib/client";

    let {cpuInfo}: { cpuInfo: CPUInfo } = $props();
</script>

<Card>
    <div class="flex flex-row items-center justify-between space-y-0 pb-2">
        <h3 class="text-sm font-medium">CPU Information</h3>
        <Cpu size={16}/>
    </div>
    <div class="space-y-3">
        <div class="space-y-1">
            <p class="text-sm font-medium">Processor</p>
            <p class="text-sm text-muted-foreground">{cpuInfo.brand}</p>
        </div>
        <div class="space-y-1">
            <p class="text-sm font-medium">Cores</p>
            <p class="text-sm text-muted-foreground">
                {cpuInfo.cores.physical} Physical / {cpuInfo.cores.logical} Logical
            </p>
        </div>
        <div class="space-y-1">
            <p class="text-sm font-medium">Frequency</p>
            <p class="text-sm text-muted-foreground">
                Current: {cpuInfo.frequency.current}GHz
                <br/>
                Range: {cpuInfo.frequency.min}GHz - {cpuInfo.frequency.max}GHz
            </p>
        </div>
    </div>
</Card>
