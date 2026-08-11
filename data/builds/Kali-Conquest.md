---
type: smite-build
god: Kali
mode: Conquest
builds:
- source: community
  aspect: Aspect of Unbound Destruction
  aspect_pick_rate: 0.38
  aspect_win_rate: 0.53
  slot_order:
  - name: Tyrfing
    pick_rate: 0.35
    win_rate: 0.53
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.15
      win_rate: 0.58
    - name: Book of Thoth
      pick_rate: 0.08
      win_rate: 0.45
  - name: Odysseus' Bow
    pick_rate: 0.22
    win_rate: 0.55
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.13
      win_rate: 0.52
    - name: Spear of Desolation
      pick_rate: 0.06
      win_rate: 0.56
  - name: Hastened Fatalis
    pick_rate: 0.21
    win_rate: 0.52
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.12
      win_rate: 0.54
    - name: Polynomicon
      pick_rate: 0.11
      win_rate: 0.52
  - name: Silverbranch Bow
    pick_rate: 0.14
    win_rate: 0.6
    alternates:
    - name: The Executioner
      pick_rate: 0.1
      win_rate: 0.38
    - name: Hastened Fatalis
      pick_rate: 0.09
      win_rate: 0.46
  - name: Qin's Blade
    pick_rate: 0.07
    win_rate: 0.46
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.1
      win_rate: 0.47
    - name: The Executioner
      pick_rate: 0.06
      win_rate: 0.6
  - name: Blinking Abyss
    pick_rate: 0.07
    win_rate: 0.65
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.07
      win_rate: 0.64
    - name: Hunter's Bow
      pick_rate: 0.07
      win_rate: 0.42
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.17
    win_rate: 0.55
  - name: Hunter's Cowl
    pick_rate: 0.15
    win_rate: 0.53
  - name: Archmage's Gem
    pick_rate: 0.14
    win_rate: 0.61
  source_url: https://smitebrain.com/gods/kali/
  last_verified: '2026-08-10'
  god_win_rate: 0.5226586102719033
  god_matches_won: 346
  god_matches_played: 662
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-10'
  god_matches_analyzed: 17490
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Gluttonous Grimoire
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Death Metal
  - Tyrfing
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, The Crusher, Gluttonous Grimoire, Death Metal, Lernaean
    Bow, Berserker''s Shield, Spear of Desolation, Damaru, Soul Gem, Golden Blade,
    Riptalon, Hydra''s Lament, Tekko-Kagi, Genji''s Guard, Bragi''s Harp, Dominance,
    Spear of the Magus, The Reaper, Runeforged Hammer, Bracer of The Abyss, The Cosmic
    Horror, Heartseeker, Breastplate of Valor, Pharaoh''s Curse, Demon Blade, Obsidian
    Shard, Titan''s Bane, Kinetic Cuirass, Amanita Charm, Shogun''s Ofuda, Avenging
    Blade, Musashi''s Dual Swords, Oni Hunter''s Garb, Shield Splitter, Pendulum Blade,
    Nimble Ring, Eye of Providence, Eros'' Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.49
    Tyrfing:
      total: 0.51
      efficiency: 0.46
      win: 0.53
      pick: 0.35
      fit: 0.59
    Death Metal:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.36
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.54
      win: 0.6
      pick: 0.23
      fit: 0.45
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Silverbranch Bow
  - The Crusher
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Soul Gem, Gluttonous Grimoire, Shield
    of the Phoenix, Kinetic Cuirass, Riptalon, The Crusher, Jotunn''s Revenge, Rod
    of Asclepius, Genji''s Guard, The Reaper, Pharaoh''s Curse, Oni Hunter''s Garb,
    Golden Blade, Chandra''s Grace, Blood-Bound Book, Runeforged Hammer, Breastplate
    of Valor, Bancroft''s Talon, Death Metal, Lernaean Bow, Shogun''s Ofuda, Phoenix
    Feather, Freya''s Tears, Damaru, Hydra''s Lament, Spectral Armor, Shifter''s Shield,
    Erosion, Eye of the Storm, Shield Splitter, Eye of Providence, Lifebinder, Spear
    of the Magus, Draconic Scale, Leviathan''s Hide, Yogi''s Necklace, Midgardian
    Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.49
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.54
      win: 0.6
      pick: 0.23
      fit: 0.27
    The Crusher:
      total: 0.5
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.69
    Soul Gem:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Spear of Desolation
  - Silverbranch Bow
  - Spear of the Magus
  - The Crusher
  flex_slots:
  - Spear of Desolation
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
    for this god: The Crusher, Jotunn''s Revenge, Gluttonous Grimoire, Spear of Desolation,
    Soul Gem, Riptalon, Spear of the Magus, Tekko-Kagi, The Cosmic Horror, The Reaper,
    Berserker''s Shield, Death Metal, Lernaean Bow, Heartseeker, Avenging Blade, Damaru,
    Obsidian Shard, Genji''s Guard, Hydra''s Lament, Golden Blade, Titan''s Bane,
    Runeforged Hammer, Screeching Gargoyle, Breastplate of Valor, Doom Orb, The World
    Stone, Pendulum Blade, Dominance, Bragi''s Harp, Dreamer''s Idol, Toxic Blade,
    Bracer of The Abyss, Pharaoh''s Curse, Stone of Binding, Kinetic Cuirass, Void
    Shield, Amanita Charm, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.61
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.53
    Spear of Desolation:
      total: 0.52
      efficiency: 0.52
      win: 0.58
      pick: 0.15
      fit: 0.47
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.54
      win: 0.6
      pick: 0.23
      fit: 0.57
    Spear of the Magus:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.43
    The Crusher:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.67
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Tyrfing
  - Gluttonous Grimoire
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - The Crusher
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
    this god: Riptalon, Gluttonous Grimoire, Berserker''s Shield, The Crusher, Jotunn''s
    Revenge, Golden Blade, Soul Gem, Lernaean Bow, Spear of Desolation, Death Metal,
    Genji''s Guard, Damaru, Hydra''s Lament, Bracer of The Abyss, Pharaoh''s Curse,
    Spear of the Magus, Tekko-Kagi, Dominance, The Reaper, Breastplate of Valor, Bragi''s
    Harp, Toxic Blade, The Cosmic Horror, Runeforged Hammer, Nimble Ring, Blood-Bound
    Book, Kinetic Cuirass, Shogun''s Ofuda, Bancroft''s Talon, Amanita Charm, Oni
    Hunter''s Garb, Obsidian Shard, Eye of Providence, Eros'' Bow, Heartseeker, Demon
    Blade, Freya''s Tears, Helm of Radiance.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.26
    Tyrfing:
      total: 0.52
      efficiency: 0.46
      win: 0.53
      pick: 0.35
      fit: 0.67
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.37
    Riptalon:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.65
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.54
      win: 0.6
      pick: 0.23
      fit: 0.57
    The Crusher:
      total: 0.5
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Hydra's Lament
  - Spear of Desolation
  - Silverbranch Bow
  - Soul Gem
  flex_slots:
  - Silverbranch Bow
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Spear of Desolation,
    Soul Gem, Genji''s Guard, Hydra''s Lament, Breastplate of Valor, Gluttonous Grimoire,
    The Crusher, Berserker''s Shield, Chronos'' Pendant, Freya''s Tears, Death Metal,
    Shield of the Phoenix, Spear of the Magus, Lernaean Bow, Gem of Focus, Riptalon,
    Damaru, The Cosmic Horror, Bracer of The Abyss, Screeching Gargoyle, Chandra''s
    Grace, Arondight, Pendulum Blade, Golden Blade, Bragi''s Harp, Obsidian Shard,
    Pharaoh''s Curse, Runeforged Hammer, Kinetic Cuirass, Amanita Charm, Blood-Bound
    Book, Tekko-Kagi, Oni Hunter''s Garb, Dominance, Helm of Radiance, The Reaper,
    Bancroft''s Talon.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.59
    Hydra's Lament:
      total: 0.51
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.55
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.58
      pick: 0.15
      fit: 0.59
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.54
      win: 0.6
      pick: 0.23
      fit: 0.31
    Soul Gem:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Lernaean Bow
  - Berserker's Shield
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
    Underrated for this god: Jotunn''s Revenge, The Crusher, Gluttonous Grimoire,
    Death Metal, Lernaean Bow, Berserker''s Shield, Damaru, Soul Gem, Golden Blade,
    Riptalon, Hydra''s Lament, Tekko-Kagi, Genji''s Guard, Bragi''s Harp, Dominance,
    Spear of the Magus, The Reaper, Runeforged Hammer, Bracer of The Abyss, The Cosmic
    Horror, Heartseeker, Breastplate of Valor, Pharaoh''s Curse, Demon Blade, Spear
    of Desolation, Obsidian Shard, Titan''s Bane, Kinetic Cuirass, Amanita Charm,
    Shogun''s Ofuda, Avenging Blade, Musashi''s Dual Swords, Oni Hunter''s Garb, Shield
    Splitter, Pendulum Blade, Nimble Ring, Eye of Providence, Eros'' Bow.'
  slot_scores:
    Lernaean Bow:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.49
    Death Metal:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.36
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: *id001
---
