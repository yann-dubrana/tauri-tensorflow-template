<script lang="ts">
    import {MonitorIcon} from "lucide-svelte";
    import {Card} from "flowbite-svelte";
    import type {OSInfo} from "$lib/client";


    let {systemInfo, pythonVersion}: { systemInfo: OSInfo; pythonVersion: string } = $props();
</script>

<Card>
    <div class="flex flex-row items-center justify-between space-y-0 pb-2">
        <h3 class="text-sm font-medium">Operating System</h3>
        <MonitorIcon size={16}/>
    </div>
    <div class="space-y-3">
        <div class="space-y-1">
            <p class="text-sm font-medium">System</p>
            <p class="text-sm text-muted-foreground">{systemInfo.system} {systemInfo.machine}</p>
        </div>
        <div class="space-y-1">
            <p class="text-sm font-medium">Version</p>
            <p class="text-sm text-muted-foreground">{systemInfo.release}</p>
        </div>
        <div class="space-y-1">
            <p class="text-sm font-medium">Python Version</p>
            <p class="text-sm text-muted-foreground">{pythonVersion}</p>
        </div>
    </div>
</Card>
