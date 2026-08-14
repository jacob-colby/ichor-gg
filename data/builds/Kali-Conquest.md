---
type: smite-build
god: Kali
mode: Conquest
builds:
- source: community
  aspect: Aspect of Unbound Destruction
  aspect_pick_rate: 0.38
  aspect_win_rate: 0.58
  slot_order:
  - name: Tyrfing
    pick_rate: 0.44
    win_rate: 0.62
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.16
      win_rate: 0.14
    - name: Book of Thoth
      pick_rate: 0.13
      win_rate: 0.55
  - name: Odysseus' Bow
    pick_rate: 0.18
    win_rate: 0.63
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.15
      win_rate: 0.62
    - name: The Cosmic Horror
      pick_rate: 0.1
      win_rate: 0.56
  - name: Hastened Fatalis
    pick_rate: 0.14
    win_rate: 0.67
    alternates:
    - name: Polynomicon
      pick_rate: 0.11
      win_rate: 0.3
    - name: Odysseus' Bow
      pick_rate: 0.1
      win_rate: 0.56
  - name: Totem of Death
    pick_rate: 0.13
    win_rate: 0.64
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.13
      win_rate: 0.18
    - name: The Executioner
      pick_rate: 0.1
      win_rate: 0.33
  - name: Rod of Tahuti
    pick_rate: 0.13
    win_rate: 0.7
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.1
      win_rate: 0.63
    - name: Qin's Blade
      pick_rate: 0.1
      win_rate: 0.38
  - name: Blinking Abyss
    pick_rate: 0.2
    win_rate: 0.55
    alternates:
    - name: Riptalon
      pick_rate: 0.07
      win_rate: 0.25
    - name: Silverbranch Bow
      pick_rate: 0.07
      win_rate: 0.75
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.26
    win_rate: 0.57
  - name: Death's Embrace
    pick_rate: 0.15
    win_rate: 0.69
  - name: Hunter's Cowl
    pick_rate: 0.14
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/kali/
  last_verified: '2026-08-14'
  god_win_rate: 0.48863636363636365
  god_matches_won: 43
  god_matches_played: 88
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-14'
  god_matches_analyzed: 3454
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
  - Gluttonous Grimoire
  - Death Metal
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
    Bow, Berserker''s Shield, Damaru, Soul Gem, Golden Blade, Hydra''s Lament, Tekko-Kagi,
    Genji''s Guard, The Cosmic Horror, Bragi''s Harp, Dominance, Spear of the Magus,
    The Reaper, Runeforged Hammer, Bracer of The Abyss, Breastplate of Valor, Heartseeker,
    Pharaoh''s Curse, Demon Blade, Obsidian Shard, Deathbringer, Titan''s Bane, Kinetic
    Cuirass, Shogun''s Ofuda, Amanita Charm, Oni Hunter''s Garb, Avenging Blade, Pendulum
    Blade, Nimble Ring, Shield Splitter, Eye of Providence, Eros'' Bow, Musashi''s
    Dual Swords.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.49
    Tyrfing:
      total: 0.55
      efficiency: 0.46
      win: 0.62
      pick: 0.44
      fit: 0.59
    Death Metal:
      total: 0.53
      efficiency: 0.58
      win: 0.56
      pick: 0.0
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.36
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.54
      win: 0.63
      pick: 0.22
      fit: 0.45
    The Crusher:
      total: 0.55
      efficiency: 0.63
      win: 0.56
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
  - The Crusher
  - Silverbranch Bow
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
    of the Phoenix, Kinetic Cuirass, The Crusher, Jotunn''s Revenge, Rod of Asclepius,
    Genji''s Guard, The Reaper, Pharaoh''s Curse, Oni Hunter''s Garb, Golden Blade,
    Chandra''s Grace, Blood-Bound Book, Breastplate of Valor, Bancroft''s Talon, Runeforged
    Hammer, Lernaean Bow, Death Metal, Shogun''s Ofuda, Freya''s Tears, Phoenix Feather,
    Damaru, Spectral Armor, Hydra''s Lament, Shifter''s Shield, Erosion, Eye of the
    Storm, Shield Splitter, The Cosmic Horror, Eye of Providence, Lifebinder, Spear
    of the Magus, Draconic Scale, Leviathan''s Hide, Yogi''s Necklace, Midgardian
    Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.49
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.54
      win: 0.63
      pick: 0.22
      fit: 0.27
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.57
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.69
    Soul Gem:
      total: 0.54
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Gluttonous Grimoire
  - Silverbranch Bow
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Rod of Tahuti
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Jotunn''s Revenge, Gluttonous Grimoire, Soul Gem, The
    Cosmic Horror, Spear of the Magus, Tekko-Kagi, Berserker''s Shield, The Reaper,
    Lernaean Bow, Death Metal, Heartseeker, Avenging Blade, Damaru, Obsidian Shard,
    Genji''s Guard, Hydra''s Lament, Golden Blade, Titan''s Bane, Screeching Gargoyle,
    Breastplate of Valor, Runeforged Hammer, The World Stone, Doom Orb, Pendulum Blade,
    Dreamer''s Idol, Dominance, Bracer of The Abyss, Toxic Blade, Bragi''s Harp, Pharaoh''s
    Curse, Stone of Binding, Kinetic Cuirass, Void Shield, Amanita Charm, Oni Hunter''s
    Garb, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.61
    Tyrfing:
      total: 0.53
      efficiency: 0.46
      win: 0.62
      pick: 0.44
      fit: 0.48
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.53
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.54
      win: 0.63
      pick: 0.22
      fit: 0.57
    The Crusher:
      total: 0.57
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.67
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.44
      win: 0.7
      pick: 0.28
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Gluttonous Grimoire
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - The Crusher
  - Jotunn's Revenge
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
    this god: Gluttonous Grimoire, Berserker''s Shield, The Crusher, Jotunn''s Revenge,
    Golden Blade, Soul Gem, Lernaean Bow, Genji''s Guard, Death Metal, Damaru, Hydra''s
    Lament, Bracer of The Abyss, The Cosmic Horror, Pharaoh''s Curse, Spear of the
    Magus, Breastplate of Valor, Tekko-Kagi, Dominance, The Reaper, Bragi''s Harp,
    Toxic Blade, Nimble Ring, Runeforged Hammer, Blood-Bound Book, Kinetic Cuirass,
    Shogun''s Ofuda, Bancroft''s Talon, Amanita Charm, Oni Hunter''s Garb, Obsidian
    Shard, Eros'' Bow, Eye of Providence, Heartseeker, Freya''s Tears, Demon Blade,
    Helm of Radiance.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.31
    Tyrfing:
      total: 0.56
      efficiency: 0.46
      win: 0.62
      pick: 0.44
      fit: 0.67
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.37
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.54
      win: 0.63
      pick: 0.22
      fit: 0.57
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Totem of Death
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Genji''s
    Guard, Hydra''s Lament, Breastplate of Valor, Gluttonous Grimoire, The Crusher,
    Berserker''s Shield, Chronos'' Pendant, Freya''s Tears, Death Metal, The Cosmic
    Horror, Shield of the Phoenix, Spear of the Magus, Lernaean Bow, Gem of Focus,
    Damaru, Screeching Gargoyle, Bracer of The Abyss, Chandra''s Grace, Arondight,
    Pendulum Blade, Golden Blade, Obsidian Shard, Pharaoh''s Curse, Bragi''s Harp,
    Kinetic Cuirass, Runeforged Hammer, Amanita Charm, Blood-Bound Book, Oni Hunter''s
    Garb, Bancroft''s Talon, Helm of Radiance, Tekko-Kagi, Dominance, The Reaper.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.56
      pick: 0.0
      fit: 0.34
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.59
    Hydra's Lament:
      total: 0.53
      efficiency: 0.58
      win: 0.56
      pick: 0.0
      fit: 0.55
    Totem of Death:
      total: 0.54
      efficiency: 0.49
      win: 0.64
      pick: 0.22
      fit: 0.45
    Soul Gem:
      total: 0.56
      efficiency: 0.59
      win: 0.56
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
    Hydra''s Lament, Tekko-Kagi, Genji''s Guard, Bragi''s Harp, Dominance, Spear of
    the Magus, The Reaper, The Cosmic Horror, Runeforged Hammer, Bracer of The Abyss,
    Breastplate of Valor, Heartseeker, Pharaoh''s Curse, Demon Blade, Obsidian Shard,
    Deathbringer, Titan''s Bane, Kinetic Cuirass, Shogun''s Ofuda, Amanita Charm,
    Oni Hunter''s Garb, Avenging Blade, Pendulum Blade, Nimble Ring, Shield Splitter,
    Eye of Providence, Eros'' Bow, Musashi''s Dual Swords.'
  slot_scores:
    Lernaean Bow:
      total: 0.53
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.49
    Death Metal:
      total: 0.53
      efficiency: 0.58
      win: 0.56
      pick: 0.0
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.36
    The Crusher:
      total: 0.55
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.55
  starter: *id001
---
