---
type: smite-build
god: Nut
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Cosmos
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.25
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.42
    win_rate: 0.58
    alternates:
    - name: Tyrfing
      pick_rate: 0.39
      win_rate: 0.34
    - name: Bragi's Harp
      pick_rate: 0.04
      win_rate: 0.67
  - name: Bragi's Harp
    pick_rate: 0.25
    win_rate: 0.38
    alternates:
    - name: Staff of Myrddin
      pick_rate: 0.17
      win_rate: 0.68
    - name: Book of Thoth
      pick_rate: 0.08
      win_rate: 0.5
  - name: Rod of Tahuti
    pick_rate: 0.14
    win_rate: 0.52
    alternates:
    - name: Soul Gem
      pick_rate: 0.12
      win_rate: 0.47
    - name: Barbed Carver
      pick_rate: 0.12
      win_rate: 0.53
  - name: The Executioner
    pick_rate: 0.14
    win_rate: 0.43
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.16
      win_rate: 0.48
    - name: Obsidian Shard
      pick_rate: 0.13
      win_rate: 0.6
  - name: Obsidian Shard
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: The Executioner
      pick_rate: 0.08
      win_rate: 0.36
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 0.67
  - name: Evil Eye
    pick_rate: 0.06
    win_rate: 0.33
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.06
      win_rate: 0.5
    - name: Void Shard
      pick_rate: 0.04
      win_rate: 0.25
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.26
    win_rate: 0.37
  - name: Archmage's Gem
    pick_rate: 0.18
    win_rate: 0.52
  - name: Bluestone Brooch
    pick_rate: 0.16
    win_rate: 0.62
  source_url: https://smitebrain.com/gods/nut/
  last_verified: '2026-08-14'
  god_win_rate: 0.44242424242424244
  god_matches_won: 73
  god_matches_played: 165
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-14'
  god_matches_analyzed: 3454
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Crusher
  - Obsidian Shard
  flex_slots:
  - Berserker's Shield
  - Obsidian Shard
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, Riptalon, Berserker''s
    Shield, Spear of the Magus, Lernaean Bow, Bracer of The Abyss, Genji''s Guard,
    The Cosmic Horror, Hydra''s Lament, Silverbranch Bow, Death Metal, Nimble Ring,
    Golden Blade, Blood-Bound Book, Breastplate of Valor, The Reaper, Bancroft''s
    Talon, Tekko-Kagi, Chronos'' Pendant, Dominance, Pharaoh''s Curse, Helm of Radiance,
    Runeforged Hammer, The World Stone, Doom Orb, Damaru, Rod of Asclepius, Dreamer''s
    Idol, Jade Scepter, Heartseeker, Kinetic Cuirass, Gem of Focus, Shogun''s Ofuda,
    Freya''s Tears.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.48
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.45
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.58
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.58
      pick: 0.42
      fit: 0.48
    The Crusher:
      total: 0.51
      efficiency: 0.63
      win: 0.48
      pick: 0.0
      fit: 0.45
    Obsidian Shard:
      total: 0.49
      efficiency: 0.54
      win: 0.5
      pick: 0.28
      fit: 0.38
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Spear of Desolation
  - The Crusher
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, Riptalon, Genji''s Guard,
    Spear of the Magus, Berserker''s Shield, Hydra''s Lament, The Cosmic Horror, Lernaean
    Bow, Silverbranch Bow, Breastplate of Valor, The Reaper, Bracer of The Abyss,
    Death Metal, Tekko-Kagi, Chronos'' Pendant, Golden Blade, Blood-Bound Book, Bancroft''s
    Talon, Nimble Ring, Pharaoh''s Curse, Dominance, Runeforged Hammer, Heartseeker,
    The World Stone, Doom Orb, Freya''s Tears, Dreamer''s Idol, Pendulum Blade, Damaru,
    Helm of Radiance, Gem of Focus, Kinetic Cuirass, Shield of the Phoenix, Rod of
    Asclepius.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.71
      win: 0.48
      pick: 0.0
      fit: 0.16
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.58
      pick: 0.42
      fit: 0.56
    The Crusher:
      total: 0.51
      efficiency: 0.63
      win: 0.48
      pick: 0.0
      fit: 0.5
    Obsidian Shard:
      total: 0.49
      efficiency: 0.54
      win: 0.5
      pick: 0.28
      fit: 0.4
    Soul Gem:
      total: 0.54
      efficiency: 0.59
      win: 0.47
      pick: 0.19
      fit: 0.73
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Spear of Desolation
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Berserker''s Shield, Riptalon, Shield
    of the Phoenix, Rod of Asclepius, Blood-Bound Book, Bancroft''s Talon, Jotunn''s
    Revenge, Genji''s Guard, Kinetic Cuirass, The Crusher, The Reaper, Pharaoh''s
    Curse, Chandra''s Grace, Breastplate of Valor, Oni Hunter''s Garb, Golden Blade,
    Spear of the Magus, Freya''s Tears, Lifebinder, Lernaean Bow, Shogun''s Ofuda,
    Hydra''s Lament, The Cosmic Horror, Runeforged Hammer, Bracer of The Abyss, Phoenix
    Feather, Spectral Armor, Helm of Radiance, Death Metal, Umbral Link, Silverbranch
    Bow, Jade Scepter, Shifter''s Shield, Erosion, Eye of Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.71
      win: 0.48
      pick: 0.0
      fit: 0.17
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.48
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.3
    Spear of Desolation:
      total: 0.51
      efficiency: 0.52
      win: 0.58
      pick: 0.42
      fit: 0.32
    Amanita Charm:
      total: 0.53
      efficiency: 0.63
      win: 0.48
      pick: 0.0
      fit: 0.64
    Soul Gem:
      total: 0.54
      efficiency: 0.59
      win: 0.47
      pick: 0.19
      fit: 0.79
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Spear of Desolation
  - Spear of the Magus
  - The Crusher
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Spear of the Magus
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, Riptalon, Spear
    of the Magus, The Cosmic Horror, Berserker''s Shield, Silverbranch Bow, The Reaper,
    Genji''s Guard, Tekko-Kagi, Lernaean Bow, Bracer of The Abyss, Hydra''s Lament,
    Avenging Blade, Death Metal, Screeching Gargoyle, Breastplate of Valor, The World
    Stone, Doom Orb, Dreamer''s Idol, Golden Blade, Blood-Bound Book, Heartseeker,
    Bancroft''s Talon, Nimble Ring, Chronos'' Pendant, Pharaoh''s Curse, Stone of
    Binding, Dominance, Toxic Blade, Runeforged Hammer, Helm of Radiance, Titan''s
    Bane, Pendulum Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.55
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.67
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.58
      pick: 0.42
      fit: 0.57
    Spear of the Magus:
      total: 0.5
      efficiency: 0.6
      win: 0.48
      pick: 0.0
      fit: 0.49
    The Crusher:
      total: 0.52
      efficiency: 0.63
      win: 0.48
      pick: 0.0
      fit: 0.56
    Obsidian Shard:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.28
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Spear of Desolation
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Berserker's Shield
  - Silverbranch Bow
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Riptalon, Jotunn''s Revenge, The Crusher, Berserker''s
    Shield, Silverbranch Bow, Golden Blade, Genji''s Guard, Lernaean Bow, Spear of
    the Magus, Bracer of The Abyss, The Cosmic Horror, Hydra''s Lament, Death Metal,
    Breastplate of Valor, Nimble Ring, Blood-Bound Book, Bancroft''s Talon, Pharaoh''s
    Curse, The Reaper, Tekko-Kagi, Chronos'' Pendant, Dominance, Toxic Blade, Runeforged
    Hammer, Helm of Radiance, Kinetic Cuirass, Damaru, Rod of Asclepius, Amanita Charm,
    Shogun''s Ofuda, Freya''s Tears, Oni Hunter''s Garb, Jade Scepter, The World Stone,
    Doom Orb.'
  slot_scores:
    Berserker's Shield:
      total: 0.49
      efficiency: 0.68
      win: 0.48
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.36
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.49
    Spear of Desolation:
      total: 0.52
      efficiency: 0.52
      win: 0.58
      pick: 0.42
      fit: 0.39
    Riptalon:
      total: 0.51
      efficiency: 0.56
      win: 0.48
      pick: 0.0
      fit: 0.63
    Silverbranch Bow:
      total: 0.49
      efficiency: 0.54
      win: 0.48
      pick: 0.0
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Hydra's Lament
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Gluttonous Grimoire, Hydra''s Lament, Breastplate of Valor, The Crusher, Berserker''s
    Shield, Riptalon, Chronos'' Pendant, Freya''s Tears, Lernaean Bow, Spear of the
    Magus, Shield of the Phoenix, Silverbranch Bow, Bracer of The Abyss, The Cosmic
    Horror, Gem of Focus, Totem of Death, Screeching Gargoyle, Golden Blade, Chandra''s
    Grace, Pendulum Blade, Pharaoh''s Curse, Death Metal, The Reaper, Arondight, Blood-Bound
    Book, Nimble Ring, Bancroft''s Talon, Tekko-Kagi, Dominance, Kinetic Cuirass,
    Runeforged Hammer, Amanita Charm, Oni Hunter''s Garb, Damaru.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.48
      pick: 0.0
      fit: 0.34
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.6
    Hydra's Lament:
      total: 0.5
      efficiency: 0.58
      win: 0.48
      pick: 0.0
      fit: 0.54
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.58
      pick: 0.42
      fit: 0.6
    Soul Gem:
      total: 0.54
      efficiency: 0.59
      win: 0.47
      pick: 0.19
      fit: 0.78
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Spear of the Magus
  - The Crusher
  flex_slots:
  - Spear of the Magus
  - Lernaean Bow
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Jotunn''s Revenge, The Crusher,
    Riptalon, Berserker''s Shield, Spear of the Magus, Lernaean Bow, Bracer of The
    Abyss, Genji''s Guard, The Cosmic Horror, Hydra''s Lament, Silverbranch Bow, Death
    Metal, Nimble Ring, Golden Blade, Blood-Bound Book, Breastplate of Valor, The
    Reaper, Bancroft''s Talon, Tekko-Kagi, Chronos'' Pendant, Dominance, Pharaoh''s
    Curse, Helm of Radiance, Runeforged Hammer, The World Stone, Doom Orb, Damaru,
    Rod of Asclepius, Dreamer''s Idol, Jade Scepter, Heartseeker, Kinetic Cuirass,
    Gem of Focus, Shogun''s Ofuda, Freya''s Tears.'
  slot_scores:
    Lernaean Bow:
      total: 0.48
      efficiency: 0.54
      win: 0.48
      pick: 0.0
      fit: 0.52
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.48
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.45
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.58
    Spear of the Magus:
      total: 0.49
      efficiency: 0.6
      win: 0.48
      pick: 0.0
      fit: 0.38
    The Crusher:
      total: 0.51
      efficiency: 0.63
      win: 0.48
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Spear of Desolation
  - Spear of the Magus
  - The Crusher
  flex_slots:
  - Spear of the Magus
  - Spear of Desolation
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
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Jotunn''s Revenge,
    The Crusher, Riptalon, Berserker''s Shield, Spear of the Magus, Lernaean Bow,
    Bracer of The Abyss, Genji''s Guard, The Cosmic Horror, Hydra''s Lament, Silverbranch
    Bow, Death Metal, Nimble Ring, Golden Blade, Blood-Bound Book, Breastplate of
    Valor, The Reaper, Bancroft''s Talon, Tekko-Kagi, Chronos'' Pendant, Dominance,
    Pharaoh''s Curse, Helm of Radiance, Runeforged Hammer, The World Stone, Doom Orb,
    Damaru, Rod of Asclepius, Dreamer''s Idol, Jade Scepter, Heartseeker, Kinetic
    Cuirass, Gem of Focus, Shogun''s Ofuda, Freya''s Tears.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.48
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.45
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.58
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.58
      pick: 0.42
      fit: 0.48
    Spear of the Magus:
      total: 0.49
      efficiency: 0.6
      win: 0.48
      pick: 0.0
      fit: 0.38
    The Crusher:
      total: 0.51
      efficiency: 0.63
      win: 0.48
      pick: 0.0
      fit: 0.45
  swaps:
  - added: Spear of Desolation
    removed: Lernaean Bow
    reason: community 58% win over 69 matches (vs 44% on this god), taking the model's
      weakest slot from Lernaean Bow
  starter: *id001
---
