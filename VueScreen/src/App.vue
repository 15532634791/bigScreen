<template>
    <div id="app" style="width: 100%">
        <router-view></router-view>
    </div>

</template>

<script setup lang="ts">

</script>
<style>
    #app{
        height: 900px;
    }
    .leftTop {
        width: 100%;
        height: 100%;
        border: 1px solid #0D2451;
        position: relative;
    }
    .angle1 {
        display: inline-block;
        position: absolute;
        width: 10px;
        height: 10px;
        top: 0;
        left: 0;
        border-top: 1px solid #1C5AB3;
        border-left: 1px solid #1C5AB3;

    }

    .angle2 {
        display: inline-block;
        position: absolute;
        width: 10px;
        height: 10px;
        top: 0;
        right: 0;
        border-top: 1px solid #1C5AB3;
        border-right: 1px solid #1C5AB3;

    }

    .angle3 {
        display: inline-block;
        position: absolute;
        width: 10px;
        height: 10px;
        bottom: 0;
        left: 0;
        border-bottom: 1px solid #1C5AB3;
        border-left: 1px solid #1C5AB3;

    }

    .angle4 {
        display: inline-block;
        position: absolute;
        width: 10px;
        height: 10px;
        bottom: 0;
        right: 0;
        border-bottom: 1px solid #1C5AB3;
        border-right: 1px solid #1C5AB3;

    }
</style>

