import nvidia_smi


class GPULoad:
    """
    Class that allows to get gpu usage
    """

    @staticmethod
    def get():
        handles = []
        output = []
        for device_id in nvidia_smi.nvmlDeviceGetCount():
            handles.append(nvidia_smi.nvmlDeviceGetHandleByIndex(device_id))
        for handle in handles:
            res = nvidia_smi.nvmlDeviceGetUtilizationRates(handle)
            output.append({
                'usage': res.gpu,
                'memory': res.memory
            })
        return output
