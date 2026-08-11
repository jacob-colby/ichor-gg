---
type: smite-build
god: Nemesis
mode: Conquest
builds:
- source: community
  aspect: Aspect of Justice
  aspect_pick_rate: 0.11
  aspect_win_rate: 0.56
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.36
    win_rate: 0.53
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.3
      win_rate: 0.6
    - name: Avenging Blade
      pick_rate: 0.05
      win_rate: 0.35
  - name: Hydra's Lament
    pick_rate: 0.24
    win_rate: 0.45
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.11
      win_rate: 0.58
    - name: Dagger of Frenzy
      pick_rate: 0.08
      win_rate: 0.5
  - name: The Reaper
    pick_rate: 0.11
    win_rate: 0.63
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.09
      win_rate: 0.6
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.6
  - name: Heartseeker
    pick_rate: 0.15
    win_rate: 0.51
    alternates:
    - name: Titan's Bane
      pick_rate: 0.09
      win_rate: 0.55
    - name: Blinking Abyss
      pick_rate: 0.09
      win_rate: 0.6
  - name: Blinking Abyss
    pick_rate: 0.08
    win_rate: 0.54
    alternates:
    - name: Heartseeker
      pick_rate: 0.1
      win_rate: 0.65
    - name: Titan's Bane
      pick_rate: 0.08
      win_rate: 0.5
  - name: Lucerne Hammer
    pick_rate: 0.08
    win_rate: 0.55
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.08
      win_rate: 0.71
    - name: Titan's Bane
      pick_rate: 0.05
      win_rate: 0.47
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.3
    win_rate: 0.58
  - name: Bumba's Cudgel
    pick_rate: 0.24
    win_rate: 0.46
  - name: Hunter's Cowl
    pick_rate: 0.11
    win_rate: 0.65
  source_url: https://smitebrain.com/gods/nemesis/
  last_verified: '2026-08-10'
  god_win_rate: 0.5274542429284526
  god_matches_won: 317
  god_matches_played: 601
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
  - Lernaean Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - The Reaper
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Gluttonous Grimoire, Death Metal, Lernaean Bow, Berserker''s
    Shield, Damaru, Soul Gem, Golden Blade, Riptalon, Tekko-Kagi, Silverbranch Bow,
    Genji''s Guard, Bragi''s Harp, Dominance, Spear of the Magus, Tyrfing, Runeforged
    Hammer, Bracer of The Abyss, The Cosmic Horror, Breastplate of Valor, Pharaoh''s
    Curse, Demon Blade, Spear of Desolation, Obsidian Shard, Kinetic Cuirass, Amanita
    Charm, Shogun''s Ofuda, Musashi''s Dual Swords, Oni Hunter''s Garb, Shield Splitter,
    Pendulum Blade, Nimble Ring, Eye of Providence, Eros'' Bow, Avenging Blade.'
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
      total: 0.56
      efficiency: 0.66
      win: 0.53
      pick: 0.36
      fit: 0.49
    Death Metal:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.51
    The Reaper:
      total: 0.54
      efficiency: 0.52
      win: 0.63
      pick: 0.17
      fit: 0.44
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.54
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Reaper
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Kinetic Cuirass
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
    this god: Amanita Charm, Berserker''s Shield, Soul Gem, Shifter''s Shield, Gluttonous
    Grimoire, Shield of the Phoenix, Kinetic Cuirass, Riptalon, The Crusher, Rod of
    Asclepius, Genji''s Guard, Pharaoh''s Curse, Oni Hunter''s Garb, Golden Blade,
    Blood-Bound Book, Chandra''s Grace, Runeforged Hammer, Breastplate of Valor, Bancroft''s
    Talon, Death Metal, Lernaean Bow, Shogun''s Ofuda, Phoenix Feather, Freya''s Tears,
    Damaru, Spectral Armor, Erosion, Eye of the Storm, Shield Splitter, Eye of Providence,
    Lifebinder, Spear of the Magus, Draconic Scale, Leviathan''s Hide, Silverbranch
    Bow, Yogi''s Necklace, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.36
      fit: 0.3
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.49
    The Reaper:
      total: 0.56
      efficiency: 0.52
      win: 0.63
      pick: 0.17
      fit: 0.57
    Shifter's Shield:
      total: 0.52
      efficiency: 0.52
      win: 0.6
      pick: 0.14
      fit: 0.39
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Silverbranch Bow
  - Spear of the Magus
  - The Crusher
  - Heartseeker
  flex_slots:
  - Spear of the Magus
  - Heartseeker
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
    for this god: The Crusher, Gluttonous Grimoire, Soul Gem, Riptalon, Silverbranch
    Bow, Spear of the Magus, Tekko-Kagi, The Cosmic Horror, Berserker''s Shield, Death
    Metal, Lernaean Bow, Damaru, Obsidian Shard, Spear of Desolation, Genji''s Guard,
    Golden Blade, Runeforged Hammer, Screeching Gargoyle, Breastplate of Valor, Doom
    Orb, The World Stone, Pendulum Blade, Dominance, Bragi''s Harp, Dreamer''s Idol,
    Toxic Blade, Bracer of The Abyss, Tyrfing, Pharaoh''s Curse, Stone of Binding,
    Kinetic Cuirass, Void Shield, Amanita Charm, Avatar''s Parashu, Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.66
      win: 0.53
      pick: 0.36
      fit: 0.61
    The Reaper:
      total: 0.56
      efficiency: 0.52
      win: 0.63
      pick: 0.17
      fit: 0.57
    Silverbranch Bow:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.0
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
    Heartseeker:
      total: 0.5
      efficiency: 0.45
      win: 0.51
      pick: 0.25
      fit: 0.67
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - The Reaper
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - The Crusher
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
    this god: Riptalon, Gluttonous Grimoire, Berserker''s Shield, The Crusher, Silverbranch
    Bow, Golden Blade, Soul Gem, Lernaean Bow, Tyrfing, Death Metal, Genji''s Guard,
    Damaru, Bracer of The Abyss, Pharaoh''s Curse, Spear of the Magus, Tekko-Kagi,
    Dominance, Breastplate of Valor, Bragi''s Harp, Toxic Blade, The Cosmic Horror,
    Runeforged Hammer, Nimble Ring, Blood-Bound Book, Kinetic Cuirass, Shogun''s Ofuda,
    Bancroft''s Talon, Amanita Charm, Oni Hunter''s Garb, Obsidian Shard, Eye of Providence,
    Eros'' Bow, Spear of Desolation, Demon Blade, Freya''s Tears, Helm of Radiance.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.36
      fit: 0.31
    The Reaper:
      total: 0.53
      efficiency: 0.52
      win: 0.63
      pick: 0.17
      fit: 0.36
    Riptalon:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.65
    Silverbranch Bow:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.0
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
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - The Crusher
  - Soul Gem
  flex_slots:
  - Hydra's Lament
  - The Crusher
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
    + fit + win/pick). Underrated for this god: Soul Gem, Genji''s Guard, Breastplate
    of Valor, Gluttonous Grimoire, The Crusher, Spear of Desolation, Berserker''s
    Shield, Chronos'' Pendant, Freya''s Tears, Death Metal, Shield of the Phoenix,
    Spear of the Magus, Lernaean Bow, Gem of Focus, Riptalon, Damaru, The Cosmic Horror,
    Bracer of The Abyss, Screeching Gargoyle, Silverbranch Bow, Chandra''s Grace,
    Arondight, Pendulum Blade, Golden Blade, Bragi''s Harp, Obsidian Shard, Pharaoh''s
    Curse, Runeforged Hammer, Kinetic Cuirass, Amanita Charm, Blood-Bound Book, Tekko-Kagi,
    Oni Hunter''s Garb, Dominance, Helm of Radiance, Bancroft''s Talon, Tyrfing.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.34
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.53
      pick: 0.36
      fit: 0.59
    Hydra's Lament:
      total: 0.5
      efficiency: 0.58
      win: 0.45
      pick: 0.33
      fit: 0.55
    The Crusher:
      total: 0.5
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.34
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
    Underrated for this god: The Crusher, Gluttonous Grimoire, Death Metal, Lernaean
    Bow, Berserker''s Shield, Damaru, Soul Gem, Golden Blade, Riptalon, Tekko-Kagi,
    Silverbranch Bow, Genji''s Guard, Bragi''s Harp, Dominance, Spear of the Magus,
    Tyrfing, Runeforged Hammer, Bracer of The Abyss, The Cosmic Horror, Breastplate
    of Valor, Pharaoh''s Curse, Demon Blade, Spear of Desolation, Obsidian Shard,
    Kinetic Cuirass, Amanita Charm, Shogun''s Ofuda, Avenging Blade, Musashi''s Dual
    Swords, Oni Hunter''s Garb, Shield Splitter, Pendulum Blade, Nimble Ring, Eye
    of Providence, Eros'' Bow.'
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
      total: 0.56
      efficiency: 0.66
      win: 0.53
      pick: 0.36
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
      fit: 0.54
  starter: *id001
---
