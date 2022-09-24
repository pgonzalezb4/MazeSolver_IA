export function useDebounce(fnc: Function, delayMs = 500) {
  let timeout: NodeJS.Timeout | null = null;
  
  return function () {
    clearTimeout(timeout!);
    
    timeout = setTimeout(() => {
      fnc();
    }, delayMs || 500);
  };
}
