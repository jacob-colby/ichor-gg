import '@testing-library/jest-dom/vitest';
import { afterEach } from 'vitest';
import { cleanup } from '@testing-library/react';
import { flushQuery } from './lib/urlState';

afterEach(() => {
  cleanup();
  // Land any debounced URL write before resetting, so a timer from this
  // test can't fire into the next one's address bar.
  flushQuery();
  // Filter state lives in the hash query string (see lib/urlState), which makes
  // the address bar shared mutable state across a file's tests: a search typed
  // in one test would arrive pre-applied in the next. Unmounting doesn't clear
  // it, so reset it here alongside cleanup.
  window.history.replaceState(null, '', `${window.location.pathname}${window.location.search}`);
});
