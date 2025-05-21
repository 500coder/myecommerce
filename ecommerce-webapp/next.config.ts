import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: "standalone",
  experimental: {
    // turbotrace: {}, // This.
    // nftTracing: true 
  },
  
};

export default nextConfig;
module.exports = {
  allowedDevOrigins: ['local-origin.dev', '*.local-origin.dev'],
// }

// module.exports = {
  webpack: (config, _) => ({
    ...config,
    watchOptions: {
      ...config.watchOptions,
      poll: 800,
      aggregateTimeout: 300,
    },
  }),
}