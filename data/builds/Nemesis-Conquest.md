---
type: smite-build
god: Nemesis
mode: Conquest
builds:
- source: community
  aspect: Aspect of Justice
  aspect_pick_rate: 0.14
  aspect_win_rate: 0.59
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.41
    win_rate: 0.57
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.25
      win_rate: 0.39
    - name: Avenging Blade
      pick_rate: 0.08
      win_rate: 0.55
  - name: Hydra's Lament
    pick_rate: 0.29
    win_rate: 0.52
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.1
      win_rate: 0.38
    - name: Transcendence
      pick_rate: 0.09
      win_rate: 0.63
  - name: Shifter's Shield
    pick_rate: 0.13
    win_rate: 0.51
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.12
      win_rate: 0.63
    - name: The Reaper
      pick_rate: 0.09
      win_rate: 0.5
  - name: Heartseeker
    pick_rate: 0.2
    win_rate: 0.54
    alternates:
    - name: The Reaper
      pick_rate: 0.06
      win_rate: 0.54
    - name: Dominance
      pick_rate: 0.06
      win_rate: 0.52
  - name: Titan's Bane
    pick_rate: 0.13
    win_rate: 0.54
    alternates:
    - name: Heartseeker
      pick_rate: 0.1
      win_rate: 0.51
    - name: Blinking Abyss
      pick_rate: 0.07
      win_rate: 0.6
  - name: Blinking Abyss
    pick_rate: 0.1
    win_rate: 0.55
    alternates:
    - name: Skeggox
      pick_rate: 0.06
      win_rate: 0.79
    - name: Mote of Chaos
      pick_rate: 0.05
      win_rate: 0.5
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.28
    win_rate: 0.57
  - name: Bumba's Cudgel
    pick_rate: 0.25
    win_rate: 0.49
  - name: Hunter's Cowl
    pick_rate: 0.16
    win_rate: 0.59
  source_url: https://smitebrain.com/gods/nemesis/
  last_verified: '2026-08-22'
  god_win_rate: 0.5299539170506913
  god_matches_won: 230
  god_matches_played: 434
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-22'
  god_matches_analyzed: 14126
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Death Metal
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Death Metal, The Crusher, Tyrfing, Golden Blade, Berserker''s
    Shield, Tekko-Kagi, Nimble Ring, Silverbranch Bow, Lernaean Bow, Riptalon, Gluttonous
    Grimoire, Soul Gem, Bragi''s Harp, Spear of the Magus, Runeforged Hammer, Toxic
    Blade, The Reaper, Spear of Desolation, Obsidian Shard, Deathbringer, Damaru,
    Dominance, Demon Blade, Genji''s Guard, Breastplate of Valor, Avenging Blade,
    Pharaoh''s Curse, Bracer of The Abyss, Amanita Charm, Shield Splitter, Musashi''s
    Dual Swords, Kinetic Cuirass, Avatar''s Parashu, Doom Orb, The Cosmic Horror,
    Shogun''s Ofuda, Freya''s Tears.'
  slot_scores:
    Book of Thoth:
      total: 0.43
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.06
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.57
      pick: 0.41
      fit: 0.49
    Transcendence:
      total: 0.51
      efficiency: 0.53
      win: 0.63
      pick: 0.12
      fit: 0.25
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.51
    The Crusher:
      total: 0.52
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.54
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.54
      pick: 0.0
      fit: 0.26
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Death Metal
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Death Metal, Nimble Ring, Soul Gem, Gluttonous Grimoire, Transcendence,
    Spear of Desolation, The Crusher, Spear of the Magus, Berserker''s Shield, Obsidian
    Shard, Genji''s Guard, Bragi''s Harp, Breastplate of Valor, Tyrfing, Lernaean
    Bow, Golden Blade, Doom Orb, Tekko-Kagi, Runeforged Hammer, Ancient Signet, The
    World Stone, Helm of Radiance, Chronos'' Pendant, Silverbranch Bow, Bracer of
    The Abyss, The Cosmic Horror, Riptalon, Dominance, The Reaper, Ethereal Staff,
    Freya''s Tears, Wish-Granting Pearl, Rod of Asclepius, Amanita Charm, Dreamer''s
    Idol, Deathbringer, Kinetic Cuirass.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.28
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.57
      pick: 0.41
      fit: 0.52
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.63
      pick: 0.12
      fit: 0.28
    Hydra's Lament:
      total: 0.52
      efficiency: 0.54
      win: 0.52
      pick: 0.4
      fit: 0.49
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.54
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.54
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Transcendence
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Berserker''s Shield, Shield of the Phoenix,
    Soul Gem, Kinetic Cuirass, Riptalon, Ethereal Staff, Rod of Asclepius, Gluttonous
    Grimoire, The Reaper, Golden Blade, Death Metal, Runeforged Hammer, Pharaoh''s
    Curse, Nimble Ring, The Crusher, Freya''s Tears, Genji''s Guard, Phoenix Feather,
    Breastplate of Valor, Shield Splitter, Shogun''s Ofuda, Yogi''s Necklace, Chandra''s
    Grace, Eye of the Storm, Spectral Armor, Mantle Of Discord, Tyrfing, Stone of
    Binding, Lernaean Bow, Erosion, Blood-Bound Book, Toxic Blade, Silverbranch Bow,
    Eye of Providence, Spear of the Magus, Leviathan''s Hide, Tekko-Kagi.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.41
      fit: 0.3
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.49
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.6
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.63
      pick: 0.12
      fit: 0.15
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Silverbranch Bow
  - Tekko-Kagi
  - The Crusher
  - Heartseeker
  flex_slots:
  - Silverbranch Bow
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, The Crusher, Gluttonous Grimoire, Silverbranch Bow,
    Tekko-Kagi, Soul Gem, Riptalon, Spear of the Magus, Death Metal, Spear of Desolation,
    Obsidian Shard, Avenging Blade, Berserker''s Shield, The Reaper, Nimble Ring,
    Toxic Blade, Tyrfing, Golden Blade, Lernaean Bow, Stone of Binding, Doom Orb,
    The Cosmic Horror, The World Stone, Avatar''s Parashu, Screeching Gargoyle, Dreamer''s
    Idol, Runeforged Hammer, Pendulum Blade, Bragi''s Harp, Genji''s Guard, Breastplate
    of Valor, Amanita Charm, Deathbringer, Damaru, Kinetic Cuirass, Dominance, Void
    Shield, Pharaoh''s Curse.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.57
      pick: 0.41
      fit: 0.61
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.53
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.68
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.49
      win: 0.54
      pick: 0.0
      fit: 0.76
    The Crusher:
      total: 0.54
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.67
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.54
      pick: 0.33
      fit: 0.77
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Transcendence
  - Tyrfing
  - Nimble Ring
  - Riptalon
  flex_slots:
  - Tyrfing
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Nimble Ring, Berserker''s Shield, Riptalon, Tyrfing,
    Silverbranch Bow, Golden Blade, Gluttonous Grimoire, Death Metal, Soul Gem, The
    Crusher, Lernaean Bow, Tekko-Kagi, Toxic Blade, Spear of the Magus, Bragi''s Harp,
    The Reaper, Genji''s Guard, Runeforged Hammer, Breastplate of Valor, Obsidian
    Shard, Spear of Desolation, Pharaoh''s Curse, Amanita Charm, Bracer of The Abyss,
    Dominance, Kinetic Cuirass, Qin''s Blade, Shogun''s Ofuda, Freya''s Tears, Deathbringer,
    Damaru, Eye of Providence, Helm of Radiance, Demon Blade, Shield Splitter, Doom
    Orb, The Cosmic Horror.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.41
      fit: 0.31
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.63
      pick: 0.12
      fit: 0.14
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.54
      pick: 0.0
      fit: 0.67
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.39
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Soul Gem, Spear of
    Desolation, Genji''s Guard, Breastplate of Valor, Nimble Ring, Freya''s Tears,
    Death Metal, Berserker''s Shield, Gluttonous Grimoire, Chronos'' Pendant, Shield
    of the Phoenix, The Crusher, Spear of the Magus, Screeching Gargoyle, Silverbranch
    Bow, Arondight, Gem of Focus, Obsidian Shard, Tyrfing, Riptalon, Golden Blade,
    Lernaean Bow, Pendulum Blade, Totem of Death, Tekko-Kagi, Amanita Charm, Runeforged
    Hammer, Bragi''s Harp, Kinetic Cuirass, Chandra''s Grace, Helm of Radiance, Bracer
    of The Abyss, Toxic Blade, Doom Orb, The Cosmic Horror, Pharaoh''s Curse, The
    World Stone, The Reaper.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.1
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.57
      pick: 0.41
      fit: 0.59
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.63
      pick: 0.12
      fit: 0.1
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.54
      pick: 0.0
      fit: 0.24
    Soul Gem:
      total: 0.54
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Tyrfing
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Death Metal, The Crusher, Tyrfing, Golden
    Blade, Berserker''s Shield, Tekko-Kagi, Nimble Ring, Silverbranch Bow, Lernaean
    Bow, Riptalon, Gluttonous Grimoire, Soul Gem, The Reaper, Bragi''s Harp, Spear
    of the Magus, Runeforged Hammer, Toxic Blade, Spear of Desolation, Dominance,
    Obsidian Shard, Deathbringer, Damaru, Demon Blade, Genji''s Guard, Breastplate
    of Valor, Pharaoh''s Curse, Bracer of The Abyss, Amanita Charm, Shield Splitter,
    Musashi''s Dual Swords, Kinetic Cuirass, Avatar''s Parashu, Avenging Blade, Doom
    Orb, The Cosmic Horror, Shogun''s Ofuda, Freya''s Tears.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.63
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.57
      pick: 0.41
      fit: 0.49
    Tyrfing:
      total: 0.52
      efficiency: 0.48
      win: 0.54
      pick: 0.0
      fit: 0.73
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.51
    The Crusher:
      total: 0.52
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.54
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.54
      pick: 0.0
      fit: 0.26
  starter: *id001
---
